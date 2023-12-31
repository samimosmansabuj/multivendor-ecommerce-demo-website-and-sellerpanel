# Generated by Django 4.2.6 on 2023-11-02 08:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_product_image01_and_more'),
        ('account', '0007_remove_staff_is_customer_remove_staff_is_seller_and_more'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('phone_number', models.TextField()),
                ('email', models.EmailField(max_length=60)),
                ('address', models.TextField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Recieved', 'Recieved'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered')], max_length=20)),
                ('order_note', models.TextField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.customer')),
                ('order_item', models.ManyToManyField(to='order.orderitem')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.seller')),
            ],
            options={
                'ordering': ['-order_date'],
            },
        ),
    ]
