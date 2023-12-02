from django.shortcuts import render, redirect
from product.models import Product
from .models import Cart, Order, OrderItem
from account.models import Customer, User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from sslcommerz_lib import SSLCOMMERZ
from django.views.decorators.csrf import csrf_exempt
import random

# Create your views here.
# -------------------------- Customer Check Out View Start------------------------------
def check_out(request):
    user = request.user
    customer = Customer.objects.get(username=user)
    cart = Cart.objects.filter(user=user)
    context = {'customer': customer, 'cart': cart}
    
    cart_total = 0
    for cart in cart:
        prod = cart.product.discount_price
        item_quantity = cart.quantity
        cart_total += prod*item_quantity
    context['cart_total'] = cart_total
    
    return render(request, 'order/check_out.html', context)
# -------------------------- Customer Check Out View End------------------------------



# -------------------------- Customer Order View Start------------------------------
def order_process(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        ordernote = request.POST['ordernote']
        paymentmethod = request.POST['paymentmethod']
        
        user = request.user
        customer = Customer.objects.get(username=user)
        cart = Cart.objects.filter(user=user)
        
        if paymentmethod == 'Cash On Delivery':
            order_product = []
            product_seller = ''
            for cart in cart:
                product_seller = cart.product.seller
                print(product_seller)
                
                orderitem = OrderItem.objects.create(
                    product = cart.product,
                    price = cart.product.discount_price,
                    quantity = cart.quantity,
                    total_price = cart.product.discount_price * cart.quantity,
                )
                order_product.append(orderitem)
                cart.delete()
            
            orders_prod = order_product.copy()
            
            total_amount = 0
            for order_product in order_product:
                net_price = order_product.total_price
                total_amount+=net_price
            
            order = Order.objects.create(
                customer = customer,
                seller = product_seller,
                first_name = first_name,
                last_name = last_name,
                phone_number = phone_number,
                email = email,
                address = address,
                total_amount = total_amount,
                paid = False,
                status = 'Pending',
                order_note = ordernote,
            )
            order.order_item.add(*orders_prod)
            order.save()
            return redirect('my_account')
            
            
        #For SSLCommerce Process Start-------------------
        if paymentmethod == 'SSLCommerce':
            
            #Order Create Process Start-------------------------
            order_product = []
            product_seller = ''
            for cart in cart:
                product_seller = cart.product.seller
                print(product_seller)
                
                orderitem = OrderItem.objects.create(
                    product = cart.product,
                    price = cart.product.discount_price,
                    quantity = cart.quantity,
                    total_price = cart.product.discount_price * cart.quantity,
                )
                order_product.append(orderitem)
                cart.delete()
            
            orders_prod = order_product.copy()
            
            total_amount = 0
            for order_product in order_product:
                net_price = order_product.total_price
                total_amount+=net_price
            
            order = Order.objects.create(
                customer = customer,
                seller = product_seller,
                first_name = first_name,
                last_name = last_name,
                phone_number = phone_number,
                email = email,
                address = address,
                total_amount = total_amount,
                paid = False,
                status = 'Pending',
                order_note = ordernote,
            )
            order.order_item.add(*orders_prod)
            order.save()
        
            
            
        #Order Payment Process Start-------------------------
            sslcz = SSLCOMMERZ({'store_id': 'niyam6412dc52e1e89', 'store_pass': 'niyam6412dc52e1e89@ssl', 'issandbox': True})
            data = {
                'total_amount': total_amount,
                'currency': "BDT",
                'tran_id': random.randint(111111, 999999),

                'success_url': "http://127.0.0.1:8000/order/payment-success/",

                # if transaction is succesful, user will be redirected here
                
                'fail_url': "http://127.0.0.1:8000/order/fail/",
                
                # if transaction is failed, user will be redirected here
                # 'cancel_url': "http://127.0.0.1:8000/payment-cancelled",
                # after user cancels the transaction, will be redirected here
                'emi_option': "0",
                'cus_name': first_name + ' ' + last_name,
                'cus_email': email,
                'cus_phone': phone_number,
                'cus_add1': address,
                'cus_city': "Dhaka",
                'cus_country': "Bangladesh",
                'shipping_method': "NO",
                'multi_card_name': "",
                'num_of_item': 1,
                'product_name': "Test",
                'product_category': "Test Category",
                'product_profile': "general",
                'order_id': order.order_id
            }
            
            order.transaction_id = data['tran_id']
            order.save()
            
            response = sslcz.createSession(data)
            return redirect(response['GatewayPageURL'])

@csrf_exempt
def payment_success(request):
    info = request.POST
    tran_id = info['tran_id']
    
    return redirect('payment_order_process', tran_id=tran_id)

def payment_order_process(request, tran_id):
    print(tran_id)
    order = Order.objects.get(transaction_id=tran_id)
    order.paid = True
    order.status = 'Recieved'
    order.save()
    return redirect('my_account')
# -------------------------- Customer Order View End------------------------------


# -------------------------- Customer Cart View Start------------------------------
@login_required(login_url='login')
def add_to_cart(request, id):
    user = request.user
    product = Product.objects.get(id=id)
    user_cart = Cart.objects.filter(user=user)
    
    try:
        if Cart.objects.get(product=product, user=user) in user_cart:
            update_cart = Cart.objects.get(product=product)
            update_cart.quantity+=1
            update_cart.save()
            return redirect(request.META['HTTP_REFERER'])
    except:
        add_cart = Cart.objects.create(user=request.user, product=product, quantity=1)
        print(add_cart)
        add_cart.save()
        return redirect(request.META['HTTP_REFERER'])

    
def remove_cart(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])

def my_cart(request):
    if request.user.is_authenticated:
        user = request.user
        my_cart = Cart.objects.filter(user=user)
        context = {'my_cart': my_cart}
        
        if request.method == 'POST':
            add = request.POST.get('add')
            minus = request.POST.get('minus')
            print(add)
            print(minus)

            if request.POST.get('add'):
                cart_id = request.POST.get('add')
                cart = Cart.objects.get(id=cart_id)
                cart.quantity +=1
                cart.save()
            if request.POST.get('minus'):
                cart_id = request.POST.get('minus')
                cart = Cart.objects.get(id=cart_id)
                if cart.quantity > 0: 
                    cart.quantity -=1
                    cart.save()
        
        cart_total = 0
        for my_cart in my_cart:
            prod = my_cart.product.discount_price
            item_quantity = my_cart.quantity
            cart_total += prod*item_quantity
        context['cart_total'] = cart_total         
        return render(request, 'order/my_cart.html', context)

# -------------------------- Customer Cart View End------------------------------