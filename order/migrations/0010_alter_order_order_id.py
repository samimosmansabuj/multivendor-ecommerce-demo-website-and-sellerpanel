# Generated by Django 4.2.6 on 2023-11-03 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.IntegerField(db_index=True, default=38768573, editable=False, unique=True),
        ),
    ]