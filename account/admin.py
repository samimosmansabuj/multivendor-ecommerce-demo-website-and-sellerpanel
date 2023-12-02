from django.contrib import admin
from .models import User, Customer, Seller, staff

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'joined_date', 'is_staff']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'phone_number', 'date_of_birth', 'is_verified', 'username']

class SellerAdmin(admin.ModelAdmin):
    list_display = ['shop_name', 'shop_created', 'is_verified', 'username']

class StaffAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'phone_number', 'date_of_birth', 'is_verified', 'username']



admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(staff, StaffAdmin)