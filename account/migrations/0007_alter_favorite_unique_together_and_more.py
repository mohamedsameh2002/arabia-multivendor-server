# Generated by Django 5.1 on 2024-08-13 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_favorite_buyerprofile_favorite_products'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='buyerprofile',
            name='favorite_products',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='product',
        ),
    ]
