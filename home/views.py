from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product, Category, Sub_Category
from order.models import Cart

# Create your views here.
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    
    context = {'categories': categories, 'products': products}
    
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        context['cart'] = cart
        
        cart_total = 0
        for cart in cart:
            prod_price = cart.product.discount_price
            item_quantity = cart.quantity
            cart_total += prod_price*item_quantity
        context['cart_total'] = cart_total
        
    return render(request, 'home/home.html', context)
