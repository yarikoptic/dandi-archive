from celery import shared_task
from celery.utils.log import get_task_logger
from django.db import transaction
from django.db.transaction import atomic

from dandiapi.api.doi import delete_doi
from dandiapi.api.manifests import (
    write_assets_jsonld,
    write_assets_yaml,
    write_collection_jsonld,
    write_dandiset_jsonld,
    write_dandiset_yaml,
)
from dandiapi.api.models import Asset, AssetBlob, Dandiset, EmbargoedAssetBlob, Version

logger = get_task_logger(__name__)


@shared_task(queue='calculate_sha256', soft_time_limit=86_400)
@atomic
def calculate_sha256(blob_id: int) -> None:
    try:
        asset_blob = AssetBlob.objects.get(blob_id=blob_id)
        logger.info(f'Found AssetBlob {blob_id}')
    except AssetBlob.DoesNotExist:
        asset_blob = EmbargoedAssetBlob.objects.get(blob_id=blob_id)
        logger.info(f'Found EmbargoedAssetBlob {blob_id}')

    sha256 = asset_blob.blob.storage.sha256_checksum(asset_blob.blob.name)

    # TODO: Run dandi-cli validation

    asset_blob.sha256 = sha256
    asset_blob.save()

    # The newly calculated sha256 digest will be included in the metadata, so we need to revalidate
    # Note, we use `.iterator` here and delay each validation as a new task in order to keep memory
    # usage down.
    def dispatch_validation():
        for asset_id in asset_blob.assets.values_list('id', flat=True).iterator():
            # Note: while asset metadata is fairly lightweight compute-wise, memory-wise it can
            # become an issue during serialization/deserialization of the JSON blob by pydantic.
            # Therefore, we delay each validation to its own task.
            validate_asset_metadata_task.delay(asset_id)

    # Run on transaction commit
    transaction.on_commit(dispatch_validation)


@shared_task(soft_time_limit=60)
@atomic
def write_manifest_files(version_id: int) -> None:
    version: Version = Version.objects.get(id=version_id)
    logger.info('Writing manifests for version %s:%s', version.dandiset.identifier, version.version)

    write_dandiset_yaml(version)
    write_assets_yaml(version)
    write_dandiset_jsonld(version)
    write_assets_jsonld(version)
    write_collection_jsonld(version)


@shared_task(soft_time_limit=10)
@atomic
def validate_asset_metadata_task(asset_id: int) -> None:
    from dandiapi.api.services.metadata import validate_asset_metadata

    asset: Asset = Asset.objects.get(id=asset_id)
    validate_asset_metadata(asset=asset)


@shared_task(soft_time_limit=30)
@atomic
def validate_version_metadata_task(version_id: int) -> None:
    from dandiapi.api.services.metadata import validate_version_metadata

    version: Version = Version.objects.get(id=version_id)
    validate_version_metadata(version=version)


@shared_task
def delete_doi_task(doi: str) -> None:
    delete_doi(doi)


@shared_task
def unembargo_dandiset_task(dandiset_id: int):
    from dandiapi.api.services.embargo import _unembargo_dandiset

    dandiset = Dandiset.objects.get(id=dandiset_id)
    _unembargo_dandiset(dandiset)


@shared_task
@atomic
def publish_dandiset_task(dandiset_id: int):
    from dandiapi.api.services.publish import _publish_dandiset

    _publish_dandiset(dandiset_id=dandiset_id)
