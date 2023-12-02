from django.urls import path
from .views import add_to_cart, remove_cart, my_cart, check_out, order_process, payment_success, payment_order_process

urlpatterns = [
    path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('remove-cart/<int:id>/', remove_cart, name='remove_cart'),
    path('my-cart/', my_cart, name='my_cart'),
    path('check-out/', check_out, name='check_out'),
    
    path('order-process/', order_process, name='order_process'),
    path('payment-success/', payment_success, name='payment_success'),
    path('payment-order-process/<tran_id>/', payment_order_process, name='payment_order_process'),
]