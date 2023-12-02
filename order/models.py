from django.db import models
from account.models import Customer, Seller, User
from product.models import Product
import uuid
import random

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    
    def __str__(self) -> str:
        return self.user.username


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    
    
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.product.product_title} x {self.quantity}'
        # return self.product.product_title

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Recieved', 'Recieved'),
        ('Processing', 'Processing'),
        ('On The Way', 'On The Way'),
        ('Delivered', 'Delivered'),
    )
    
    order_id = models.IntegerField(default=random.randint(11111111, 99999999), unique=True, db_index=True, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    order_item = models.ManyToManyField(OrderItem)
    
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone_number = models.TextField()
    email = models.EmailField(max_length=60)
    address = models.TextField()
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)
    paid = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(choices=STATUS, max_length=20)
    order_note = models.TextField(blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, blank=True, null=True)
    
    class Meta:
        ordering = ['-order_date']
    
    def __str__(self) -> str:
        return f'Order ID: {self.order_id}'