from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from .managers import BaseManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=60, unique=True, validators=[UnicodeUsernameValidator])
    email = models.EmailField(max_length=50, unique=True)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = BaseManager()
    
    is_seller = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    
    joined_date = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        ordering = ['-joined_date']
    
    def __str__(self) -> str:
        return self.username


class staff(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.TextField()
    gender = models.CharField(choices=GENDER, max_length=10, blank=True, null=False)
    date_of_birth = models.DateField(blank=True, null=False)
    
    auth_token = models.CharField(max_length=400, blank=True)
    otp_token = models.CharField(max_length=400, blank=True)
    is_officestaff = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    
    
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Customer(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.TextField()
    gender = models.CharField(choices=GENDER, max_length=10, blank=True, null=False)
    date_of_birth = models.DateField(blank=True, null=True)
    customer_profile_pic = models.ImageField(upload_to='customer/profile_pic/')
    address = models.TextField()
    address_district = models.CharField(blank=True, null=True, max_length=40)
    address_country = models.CharField(blank=True, null=True, max_length=40)
    
    auth_token = models.CharField(max_length=400, blank=True, null=True)
    otp_token = models.CharField(max_length=400, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Seller(User):
    shop_name = models.CharField(max_length=300, unique=True)
    shop_created = models.DateField(auto_now_add=True)
    shop_address = models.TextField()
    shop_logo = models.ImageField(upload_to='seller/shop_logo', blank=True, null=False)
    shop_banner = models.ImageField(upload_to='seller/shop_banner', blank=True, null=False)
    phone_number = models.TextField(blank=True, null=True)
    
    auth_token = models.CharField(max_length=400, blank=True, null=True)
    otp_token = models.CharField(max_length=400, blank=True, null=True)
    
    is_verified = models.BooleanField(default=False)
    