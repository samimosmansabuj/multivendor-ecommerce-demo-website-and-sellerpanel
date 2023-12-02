from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('registration/', Registration, name='registration'),
    path('my-account/', my_account, name='my_account'),
    
    path('view-order/<int:order_id>/', view_order, name='view_order'),
    path('download-invoice/<int:order_id>/', download_invoice, name='download_invoice'),
    
    path('verify-registration-link/<auth_token>/', verify, name='verify'),
    path('registration-verification/<int:id>/', registration_verification, name='registration_verification'),
]