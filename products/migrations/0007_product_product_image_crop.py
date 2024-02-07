# Generated by Django 4.2.3 on 2023-07-17 10:17

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_product_cropping_alter_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image_crop',
            field=image_cropping.fields.ImageRatioField('product_image', '400x400', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='product image crop'),
        ),
    ]
