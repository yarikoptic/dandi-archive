# Generated by Django 4.1.1 on 2022-11-08 17:38

from django.db import migrations, models

import dandiapi.api.storage


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_migrate_embargoed_blobs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='embargoedassetblob',
            name='dandiset',
        ),
        migrations.RemoveField(
            model_name='embargoedupload',
            name='dandiset',
        ),
        migrations.RemoveConstraint(
            model_name='asset',
            name='exactly-one-blob',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='embargoed_blob',
        ),
        migrations.AlterField(
            model_name='assetblob',
            name='blob',
            field=dandiapi.api.storage.DynamicStorageFileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='upload',
            name='blob',
            field=dandiapi.api.storage.DynamicStorageFileField(blank=True, upload_to=''),
        ),
        migrations.AddConstraint(
            model_name='asset',
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(('blob__isnull', True), ('zarr__isnull', False)),
                    models.Q(('blob__isnull', False), ('zarr__isnull', True)),
                    _connector='OR',
                ),
                name='exactly-one-blob',
            ),
        ),
        migrations.AddConstraint(
            model_name='assetblob',
            constraint=models.UniqueConstraint(
                fields=('etag', 'size', 'embargoed'), name='unique-etag-size-embargoed'
            ),
        ),
        migrations.DeleteModel(
            name='EmbargoedAssetBlob',
        ),
        migrations.DeleteModel(
            name='EmbargoedUpload',
        ),
    ]
