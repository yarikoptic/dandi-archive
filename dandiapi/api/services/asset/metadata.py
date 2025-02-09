from django.db import transaction
from django.db.models.query import QuerySet

from dandiapi.api.models.asset import Asset
from dandiapi.api.services.metadata import validate_asset_metadata


def _maybe_validate_asset_metadata(asset: Asset):
    """
    Validate asset metadata if a checksum for its blob has already been computed.

    If the checksum isn't there yet, it's the responsibility of the checksum code
    to trigger validation for all assets pointing to its blob.
    """
    if asset.is_blob:
        blob = asset.blob
    elif asset.is_embargoed_blob:
        blob = asset.embargoed_blob
    else:
        # TODO: assert? zarr?
        return

    if blob.sha256 is None:
        return

    # If the blob already has a sha256, then the asset metadata is ready to validate.
    # We do not bother to delay it because it should run very quickly.
    validate_asset_metadata(asset=asset)


def bulk_recalculate_asset_metadata(*, assets: QuerySet[Asset]):
    with transaction.atomic():
        for asset in assets.iterator():
            # populates metadata
            asset.save()
