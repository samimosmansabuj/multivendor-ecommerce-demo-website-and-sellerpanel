from django.urls import path
from .views import products, category_product, product_details

urlpatterns = [
    path('', products, name='products'),
    path('category-product/<int:id>/', category_product, name='category_product'),
    path('<slug>/', product_details, name='product_details')
]