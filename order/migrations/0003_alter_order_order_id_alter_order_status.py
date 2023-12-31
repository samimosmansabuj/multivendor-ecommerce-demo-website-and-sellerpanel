# Generated by Django 4.2.6 on 2023-11-02 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.IntegerField(db_index=True, default=93132047, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Recieved', 'Recieved'), ('Processing', 'Processing'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered')], max_length=20),
        ),
    ]
