from django.urls import path
from .views import *

urlpatterns = [
    path('', admin_panel, name='admin_panel'),
    path('add-product/', add_product, name='add_product'),
    path('update-product/<int:id>/', update_product, name='update_product'),
    path('add-product-success/<int:id>/', product_add_success, name='product_add_success'),
    path('product-list/', product_list, name='product_list'),
    
    path('registration/', seller_registratino, name='seller_registratino'),
    path('login/', Login, name='seller_login'),
    path('logout-seller/', Logout, name='seller_logout'),
    path('forget-password/', forget_password, name='forget_password'),
    
    path('order-list/', order_list, name='order_list'),
    path('order-details/<int:order_id>/', order_details, name='order_details'),
    path('order-invoice/<int:order_id>/', order_invoice, name='order_invoice'),
]