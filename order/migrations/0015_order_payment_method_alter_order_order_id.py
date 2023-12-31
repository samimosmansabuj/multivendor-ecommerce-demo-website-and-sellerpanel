# Generated by Django 4.2.6 on 2023-11-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_alter_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.IntegerField(db_index=True, default=63085115, editable=False, unique=True),
        ),
    ]
