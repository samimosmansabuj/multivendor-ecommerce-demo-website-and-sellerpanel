# Generated by Django 4.2.6 on 2023-10-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customer_seller_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='phone_number',
            field=models.TextField(blank=True, null=True),
        ),
    ]
