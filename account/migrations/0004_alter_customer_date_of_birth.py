# Generated by Django 4.2.6 on 2023-10-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_seller_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
