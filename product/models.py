from django.db import models
from account.models import Seller

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
    
    def __str__(self) -> str:
        return self.title

class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
    
    def __str__(self) -> str:
        return self.title
    

class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='product')
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.DO_NOTHING)
    
    product_title = models.CharField(max_length=300)
    product_slug = models.SlugField(max_length=300, unique=True)
    current_price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_image01 = models.ImageField(upload_to='seller/product/image/')
    product_image02 = models.ImageField(upload_to='seller/product/image/', blank=True)
    short_descriptino = models.CharField(max_length=3000)
    product_details = models.TextField()
    quantity = models.PositiveIntegerField()
    featured = models.BooleanField(default=False)
    
    is_stock = models.BooleanField(default=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self) -> str:
        return self.product_title
    
    

