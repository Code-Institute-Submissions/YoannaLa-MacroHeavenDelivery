# Generated by Django 3.2 on 2022-02-20 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_featured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='featured_image',
            new_name='image',
        ),
    ]
