# Generated by Django 4.2.6 on 2023-10-26 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_customer_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='auth_token',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='otp_token',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='auth_token',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='otp_token',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]