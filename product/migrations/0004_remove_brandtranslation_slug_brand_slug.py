# Generated by Django 5.1 on 2024-08-10 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_brandtranslation_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brandtranslation',
            name='slug',
        ),
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]