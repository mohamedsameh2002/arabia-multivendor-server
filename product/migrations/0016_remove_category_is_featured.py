# Generated by Django 5.1 on 2024-08-17 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_product_color_alter_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_featured',
        ),
    ]
