# Generated by Django 5.1 on 2024-08-17 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_remove_category_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]