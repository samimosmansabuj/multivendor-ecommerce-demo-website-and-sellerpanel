from .models import *

def quick_cart(request):
    if request.user.is_authenticated:
        user = request.user
        quickcart = Cart.objects.filter(user=user)
        context = {'quickcart': quickcart}
        cart_total = 0
        for quickcart in quickcart:
            prod_price = quickcart.product.discount_price
            item_quantity = quickcart.quantity
            cart_total+=prod_price*item_quantity
        context['cart_total'] = cart_total
        
        return context
    else:
        return {}