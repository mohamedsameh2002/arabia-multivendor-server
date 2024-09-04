# Generated by Django 5.1 on 2024-08-10 21:05

import common.utils.file_upload_paths
import common.validators.image_extension_validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_category_categorytranslation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to=common.utils.file_upload_paths.categories_images_path, validators=[common.validators.image_extension_validator.image_extension_validator], verbose_name='Category Image'),
        ),
    ]