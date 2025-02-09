# Generated by Django 4.1.1 on 2022-11-03 18:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0038_assetpath_assetpathrelation_alter_asset_path_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='assetpath',
            constraint=models.CheckConstraint(
                check=models.Q(
                    ('asset__isnull', True),
                    models.Q(('aggregate_files__lte', 1), ('asset__isnull', False)),
                    _connector='OR',
                ),
                name='consistent-leaf-paths',
            ),
        ),
    ]
