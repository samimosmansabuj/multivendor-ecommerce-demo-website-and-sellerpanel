# Generated by Django 4.2.6 on 2023-11-02 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_order_order_id_alter_order_order_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.IntegerField(db_index=True, default=96856841, editable=False, unique=True),
        ),
    ]
