# Generated by Django 4.2.6 on 2023-10-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_customer_is_customer_remove_seller_is_seller_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='is_seller',
        ),
        migrations.AddField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_seller',
            field=models.BooleanField(default=False),
        ),
    ]
