from django.contrib import admin
from .models import Product, Category, Sub_Category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'product_slug': ('product_title',)}
    list_display = ['product_title', 'current_price', 'discount_price', 'quantity', 'id', 'featured']

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'featured', 'created_date', 'id']

class Sub_CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'featured', 'created_date', 'id']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_Category, Sub_CategoryAdmin)


