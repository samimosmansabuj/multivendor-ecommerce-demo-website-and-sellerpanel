from django.contrib import admin
from .models import Cart, Order, OrderItem

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'product', 'quantity']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'first_name', 'last_name', 'phone_number', 'total_amount', 'order_date']
    
admin.site.register(Cart, CartAdmin)

admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
