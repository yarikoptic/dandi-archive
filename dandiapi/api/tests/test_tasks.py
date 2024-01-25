from __future__ import annotations

import datetime
import hashlib
from typing import TYPE_CHECKING

from django.conf import settings
from django.forms.models import model_to_dict
from django.utils import timezone
from guardian.shortcuts import assign_perm
import pytest

from dandiapi.api import tasks
from dandiapi.api.models import Asset, AssetBlob, EmbargoedAssetBlob, Version

from .fuzzy import URN_RE, UTC_ISO_TIMESTAMP_RE

if TYPE_CHECKING:
    from django.contrib.auth.models import User
    from django.core.files.storage import Storage
    from rest_framework.test import APIClient


@pytest.mark.django_db()
def test_calculate_checksum_task(storage: Storage, asset_blob_factory):
    # Pretend like AssetBlob was defined with the given storage
    AssetBlob.blob.field.storage = storage

    asset_blob = asset_blob_factory(sha256=None)

    h = hashlib.sha256()
    h.update(asset_blob.blob.read())
    sha256 = h.hexdigest()

    tasks.calculate_sha256(asset_blob.blob_id)

    asset_blob.refresh_from_db()

    assert asset_blob.sha256 == sha256


@pytest.mark.django_db()
def test_calculate_checksum_task_embargo(storage: Storage, embargoed_asset_blob_factory):
    # Pretend like EmbargoedAssetBlob was defined with the given storage
    EmbargoedAssetBlob.blob.field.storage = storage

    asset_blob = embargoed_asset_blob_factory(sha256=None)

    h = hashlib.sha256()
    h.update(asset_blob.blob.read())
    sha256 = h.hexdigest()

    tasks.calculate_sha256(asset_blob.blob_id)

    asset_blob.refresh_from_db()

    assert asset_blob.sha256 == sha256


@pytest.mark.django_db()
def test_write_manifest_files(storage: Storage, version: Version, asset_factory):
    # Pretend like AssetBlob was defined with the given storage
    # The task piggybacks off of the AssetBlob storage to write the yamls
    AssetBlob.blob.field.storage = storage

    # Create a new asset in the version so there is information to write
    version.assets.add(asset_factory())

    # All of these files should be generated by the task
    assets_yaml_path = (
        f'{settings.DANDI_DANDISETS_BUCKET_PREFIX}'
        f'dandisets/{version.dandiset.identifier}/{version.version}/assets.yaml'
    )
    dandiset_yaml_path = (
        f'{settings.DANDI_DANDISETS_BUCKET_PREFIX}'
        f'dandisets/{version.dandiset.identifier}/{version.version}/dandiset.yaml'
    )
    assets_jsonld_path = (
        f'{settings.DANDI_DANDISETS_BUCKET_PREFIX}'
        f'dandisets/{version.dandiset.identifier}/{version.version}/assets.jsonld'
    )
    dandiset_jsonld_path = (
        f'{settings.DANDI_DANDISETS_BUCKET_PREFIX}'
        f'dandisets/{version.dandiset.identifier}/{version.version}/dandiset.jsonld'
    )
    collection_jsonld_path = (
        f'{settings.DANDI_DANDISETS_BUCKET_PREFIX}'
        f'dandisets/{version.dandiset.identifier}/{version.version}/collection.jsonld'
    )

    tasks.write_manifest_files(version.id)

    assert storage.exists(assets_yaml_path)
    assert storage.exists(dandiset_yaml_path)
    assert storage.exists(assets_jsonld_path)
    assert storage.exists(dandiset_jsonld_path)
    assert storage.exists(collection_jsonld_path)


@pytest.mark.django_db()
def test_validate_asset_metadata(draft_asset: Asset):
    tasks.validate_asset_metadata_task(draft_asset.id)

    draft_asset.refresh_from_db()

    assert draft_asset.status == Asset.Status.VALID
    assert draft_asset.validation_errors == []


@pytest.mark.django_db()
def test_validate_asset_metadata_malformed_schema_version(draft_asset: Asset):
    draft_asset.metadata['schemaVersion'] = 'xxx'
    draft_asset.save()

    tasks.validate_asset_metadata_task(draft_asset.id)

    draft_asset.refresh_from_db()

    assert draft_asset.status == Asset.Status.INVALID
    assert len(draft_asset.validation_errors) == 1
    assert draft_asset.validation_errors[0]['field'] == ''
    assert draft_asset.validation_errors[0]['message'].startswith(
        'Metadata version xxx is not allowed.'
    )


@pytest.mark.django_db()
def test_validate_asset_metadata_no_encoding_format(draft_asset: Asset):
    del draft_asset.metadata['encodingFormat']
    draft_asset.save()

    tasks.validate_asset_metadata_task(draft_asset.id)

    draft_asset.refresh_from_db()

    assert draft_asset.status == Asset.Status.INVALID
    assert draft_asset.validation_errors == [
        {'field': '', 'message': "'encodingFormat' is a required property"}
    ]


@pytest.mark.django_db()
def test_validate_asset_metadata_no_digest(draft_asset: Asset):
    draft_asset.blob.sha256 = None
    draft_asset.blob.save()

    del draft_asset.full_metadata['digest']
    draft_asset.save()

    tasks.validate_asset_metadata_task(draft_asset.id)

    draft_asset.refresh_from_db()

    assert draft_asset.status == Asset.Status.INVALID
    assert draft_asset.validation_errors == [
        {'field': 'digest', 'message': 'Value error, A non-zarr asset must have a sha2_256.'}
    ]


@pytest.mark.django_db()
def test_validate_asset_metadata_malformed_keywords(draft_asset: Asset):
    draft_asset.metadata['keywords'] = 'foo'
    draft_asset.save()

    tasks.validate_asset_metadata_task(draft_asset.id)

    draft_asset.refresh_from_db()

    assert draft_asset.status == Asset.Status.INVALID
    assert draft_asset.validation_errors == [
        {'field': 'keywords', 'message': "'foo' is not of type 'array'"}
    ]


@pytest.mark.django_db()
def test_validate_asset_metadata_saves_version(draft_asset: Asset, draft_version: Version):
    draft_version.assets.add(draft_asset)

    # Update version with queryset so modified isn't auto incremented
    old_datetime = datetime.datetime.fromtimestamp(1573782390).astimezone(datetime.UTC)
    Version.objects.filter(id=draft_version.id).update(modified=old_datetime)

    # Run task
    tasks.validate_asset_metadata_task(draft_asset.id)

    # Test that version has new modified timestamp
    draft_version.refresh_from_db()
    assert draft_version.modified != old_datetime


@pytest.mark.django_db()
def test_validate_version_metadata(draft_version: Version, asset: Asset):
    draft_version.assets.add(asset)

    # Bypass .save to manually set an older timestamp
    old_modified = timezone.now() - datetime.timedelta(minutes=10)
    updated = Version.objects.filter(id=draft_version.id).update(modified=old_modified)
    assert updated == 1

    tasks.validate_version_metadata_task(draft_version.id)
    draft_version.refresh_from_db()

    assert draft_version.status == Version.Status.VALID
    assert draft_version.validation_errors == []

    # Ensure modified field was updated
    assert draft_version.modified > old_modified


@pytest.mark.django_db()
def test_validate_version_metadata_no_side_effects(draft_version: Version, asset: Asset):
    draft_version.assets.add(asset)

    # Set the version `status` and `validation_errors` fields to something
    # which can't be a result of validate_version_metadata
    draft_version.status = Version.Status.PENDING
    draft_version.validation_errors = [{'foo': 'bar'}]
    draft_version.save()

    # Validate version metadata, storing the model data before and after
    old_data = model_to_dict(draft_version)
    tasks.validate_version_metadata_task(draft_version.id)
    draft_version.refresh_from_db()
    new_data = model_to_dict(draft_version)

    # Check that change is isolated to these two fields
    assert old_data.pop('status') != new_data.pop('status')
    assert old_data.pop('validation_errors') != new_data.pop('validation_errors')
    assert old_data == new_data


@pytest.mark.django_db()
def test_validate_version_metadata_malformed_schema_version(draft_version: Version, asset: Asset):
    draft_version.assets.add(asset)

    draft_version.metadata['schemaVersion'] = 'xxx'
    draft_version.save()

    tasks.validate_version_metadata_task(draft_version.id)

    draft_version.refresh_from_db()

    assert draft_version.status == Version.Status.INVALID
    assert len(draft_version.validation_errors) == 1
    assert draft_version.validation_errors[0]['message'].startswith(
        'Metadata version xxx is not allowed.'
    )


@pytest.mark.django_db()
def test_validate_version_metadata_no_description(draft_version: Version, asset: Asset):
    draft_version.assets.add(asset)

    del draft_version.metadata['description']
    draft_version.save()

    tasks.validate_version_metadata_task(draft_version.id)

    draft_version.refresh_from_db()

    assert draft_version.status == Version.Status.INVALID
    assert draft_version.validation_errors == [
        {'field': '', 'message': "'description' is a required property"}
    ]


@pytest.mark.django_db()
def test_validate_version_metadata_malformed_license(draft_version: Version, asset: Asset):
    draft_version.assets.add(asset)

    draft_version.metadata['license'] = 'foo'
    draft_version.save()

    tasks.validate_version_metadata_task(draft_version.id)

    draft_version.refresh_from_db()

    assert draft_version.status == Version.Status.INVALID
    assert draft_version.validation_errors == [
        {'field': 'license', 'message': "'foo' is not of type 'array'"}
    ]


@pytest.mark.django_db()
def test_validate_version_metadata_no_assets(
    draft_version: Version,
):
    # Validate the metadata to mark version as `VALID`
    tasks.validate_version_metadata_task(draft_version.id)
    draft_version.refresh_from_db()
    assert draft_version.status == Version.Status.INVALID
    assert draft_version.validation_errors == [
        {
            'field': 'assetsSummary',
            'message': 'Value error, '
                       'A Dandiset containing no files or zero bytes is not publishable',
        }
    ]


@pytest.mark.django_db()
def test_publish_task(
    api_client: APIClient,
    user: User,
    draft_asset_factory,
    published_asset_factory,
    draft_version_factory,
    django_capture_on_commit_callbacks,
):
    # Create a draft_version in PUBLISHING state
    draft_version: Version = draft_version_factory(status=Version.Status.PUBLISHING)

    assign_perm('owner', user, draft_version.dandiset)
    api_client.force_authenticate(user=user)

    old_draft_asset: Asset = draft_asset_factory(status=Asset.Status.VALID)
    old_published_asset: Asset = published_asset_factory()
    assert not old_draft_asset.published
    assert old_published_asset.published

    draft_version.assets.set([old_draft_asset, old_published_asset])

    # Ensure that the number of versions increases by 1 after publishing
    starting_version_count = draft_version.dandiset.versions.count()

    with django_capture_on_commit_callbacks(execute=True):
        tasks.publish_dandiset_task(draft_version.dandiset.id)

    assert draft_version.dandiset.versions.count() == starting_version_count + 1

    draft_version.refresh_from_db()
    assert draft_version.status == Version.Status.PUBLISHED

    published_version = draft_version.dandiset.versions.latest('created')

    assert published_version.metadata == {
        **draft_version.metadata,
        'publishedBy': {
            'id': URN_RE,
            'name': 'DANDI publish',
            'startDate': UTC_ISO_TIMESTAMP_RE,
            'endDate': UTC_ISO_TIMESTAMP_RE,
            'wasAssociatedWith': [
                {
                    'id': URN_RE,
                    'identifier': 'RRID:SCR_017571',
                    'name': 'DANDI API',
                    # TODO: version the API
                    'version': '0.1.0',
                    'schemaKey': 'Software',
                }
            ],
            'schemaKey': 'PublishActivity',
        },
        'datePublished': UTC_ISO_TIMESTAMP_RE,
        'manifestLocation': [
            f'http://{settings.MINIO_STORAGE_ENDPOINT}/test-dandiapi-dandisets/test-prefix/dandisets/{draft_version.dandiset.identifier}/{published_version.version}/assets.yaml',
        ],
        'identifier': f'DANDI:{draft_version.dandiset.identifier}',
        'version': published_version.version,
        'id': f'DANDI:{draft_version.dandiset.identifier}/{published_version.version}',
        'url': (
            f'{settings.DANDI_WEB_APP_URL}/dandiset/{draft_version.dandiset.identifier}'
            f'/{published_version.version}'
        ),
        'citation': published_version.citation(published_version.metadata),
        'doi': f'10.80507/dandi.{draft_version.dandiset.identifier}/{published_version.version}',
        # Once the assets are linked, assetsSummary should be computed properly
        'assetsSummary': {
            'schemaKey': 'AssetsSummary',
            'numberOfBytes': 200,
            'numberOfFiles': 2,
            'dataStandard': [
                {
                    'schemaKey': 'StandardsType',
                    'identifier': 'RRID:SCR_015242',
                    'name': 'Neurodata Without Borders (NWB)',
                }
            ],
            'approach': [],
            'measurementTechnique': [],
            'variableMeasured': [],
            'species': [],
        },
    }

    assert published_version.assets.count() == 2
    new_draft_asset: Asset = published_version.assets.get(asset_id=old_draft_asset.asset_id)
    new_published_asset: Asset = published_version.assets.get(asset_id=old_published_asset.asset_id)

    # The former draft asset should have been modified into a published asset
    assert new_draft_asset.published
    assert new_draft_asset.asset_id == old_draft_asset.asset_id
    assert new_draft_asset.path == old_draft_asset.path
    assert new_draft_asset.blob == old_draft_asset.blob
    assert new_draft_asset.metadata == {
        **old_draft_asset.full_metadata,
        'datePublished': UTC_ISO_TIMESTAMP_RE,
        'publishedBy': {
            'id': URN_RE,
            'name': 'DANDI publish',
            'startDate': UTC_ISO_TIMESTAMP_RE,
            # TODO: endDate needs to be defined before publish is complete
            'endDate': UTC_ISO_TIMESTAMP_RE,
            'wasAssociatedWith': [
                {
                    'id': URN_RE,
                    'identifier': 'RRID:SCR_017571',
                    'name': 'DANDI API',
                    'version': '0.1.0',
                    'schemaKey': 'Software',
                }
            ],
            'schemaKey': 'PublishActivity',
        },
    }

    # The published_asset should be completely unchanged
    assert new_published_asset.published
    assert new_published_asset.asset_id == old_published_asset.asset_id
    assert new_published_asset.path == old_published_asset.path
    assert new_published_asset.blob == old_published_asset.blob
    assert new_published_asset.metadata == old_published_asset.metadata
