# Generated by Django 4.2.6 on 2023-10-31 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image01',
            field=models.ImageField(upload_to='seller/product/image/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image02',
            field=models.ImageField(blank=True, upload_to='seller/product/image/'),
        ),
    ]
