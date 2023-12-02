from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.models import Category, Sub_Category, Product
from account.models import Seller, Customer, User, staff
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from order.models import Order, OrderItem
from account.models import Seller
from xhtml2pdf import pisa
from django.template.loader import get_template


# ------------Seller Authentication Start------------
def seller_registratino(request):
    if request.method == 'POST':
        shop_name = request.POST['shop_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        phone_number = request.POST['phone_number']
        
        if password != re_password:
            pass
        else:
            seller = Seller.objects.create(shop_name=shop_name, username=username, phone_number=phone_number, email=email)
            seller.set_password(password)
            seller.is_seller = True
            seller.is_verified = True
            seller.save()
            return redirect('seller_login')
    return render(request, 'seller/account/registration.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if Seller.objects.filter(username=username).exists():
            user = authenticate(username=username, password=password)
            if not user:
                messages.warning(request, "Wrong Password!")
                return redirect('seller_login')
            else:
                login(request, user)
                return redirect('admin_panel')
        elif Customer.objects.filter(username=username).exists():
            messages.warning(request, "This is a Customer Account!")
            return redirect('seller_login')
    return render(request, 'seller/account/login.html')

def forget_password(request):
    if request.method == 'POST':
        username = request.POST['username']
    
    return render(request, 'seller/account/forget_password.html')

def Logout(request):
    logout(request)
    return redirect('seller_login')
# ------------Seller Authentication End------------




def admin_panel(request):
    if not request.user.is_authenticated:
        return redirect('seller_login')
    
    login_user = request.user
    if Seller.objects.filter(username=login_user).exists():
        seller = Seller.objects.get(username=login_user)
        products = Product.objects.filter(seller=seller)
        context = {'seller': seller, 'products': products}
        
        return render(request, 'seller/home/dashboard.html', context)
    else:
        return redirect('seller_login')



# ------------Seller Product Add, List Start------------
def add_product(request):
    categories = Category.objects.all()
    sub_categories = Sub_Category.objects.all()
    context = {'categories': categories, 'sub_categories': sub_categories}
    if request.method == 'POST':
        seller = Seller.objects.get(username=request.user)
        product_title = request.POST['product_title']
        quantity = request.POST['quantity']
        category = request.POST['category']
        sub_category = request.POST['sub_category']
        short_description = request.POST['short_description']
        product_details = request.POST['product_details']
        product_image = request.FILES['product_image']
        current_price = request.POST['current_price']
        discount_price = request.POST['discount_price']
        
        p_category = Category.objects.get(title=category)
        p_sub_category = Sub_Category.objects.get(title=sub_category)
        
        product = Product.objects.create(
            seller=seller,
            category=p_category,
            sub_category=p_sub_category,
            product_title=product_title,
            current_price=current_price,
            discount_price=discount_price,
            product_image01=product_image,
            short_descriptino=short_description,
            product_details=product_details,
            quantity=quantity,
        )
        product.featured = True
        product.save()
        return redirect('product_add_success', id=product.id)  
    return render(request, 'seller/product/add_product.html', context)

def update_product(request, id):
    product = Product.objects.get(id=id)
    categories = Category.objects.all()
    sub_categories = Sub_Category.objects.all()
    context = {'categories': categories, 'sub_categories': sub_categories, 'product': product}
    
    if request.method == 'POST':
        category = request.POST['category']
        sub_category = request.POST['sub_category']
        # prod_image = request.FILES.get['product_image']
        
        # if prod_image:
        #     product.product_image01 = prod_image
        
        product.category = Category.objects.get(title=category)
        product.sub_category = Sub_Category.objects.get(title=sub_category)
        product.product_title = request.POST['product_title']
        product.current_price = request.POST['current_price']
        product.discount_price = request.POST['discount_price']
        product.short_descriptino = request.POST['short_description']
        product.product_details = request.POST['product_details']
        product.quantity = request.POST['quantity']

        product.save()
        return redirect('product_add_success', id=product.id)
    
    return render(request, 'seller/product/update_product.html', context)

def product_add_success(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'seller/product/product_add_success.html', {'product': product})

def product_list(request):
    user = request.user
    seller = Seller.objects.get(username=user)
    product = Product.objects.filter(seller=seller)
    context = {'seller': seller, 'product': product}
    
    print(request.user.seller.shop_name)
    
    return render(request, 'seller/product/product_list.html', context)

# ------------Seller Product Add, List End------------




# ------------Seller Order List, Order Details And Invoice Start------------
def order_list(request):
    user = request.user
    if user.is_seller == False:
        return redirect('home')
    
    order = Order.objects.filter(seller=user)
    
    context = {'order': order}
    
    return render(request, 'seller/seller_order/order_list.html', context)


def order_details(request, order_id):
    order = Order.objects.get(order_id=order_id)
    orderitems = order.order_item.all()
    context = {'order': order, 'orderitems': orderitems}
    
    if request.method == 'POST':
        order_id = request.POST['order_id']
        status = request.POST['status']
        select_order = Order.objects.get(order_id=order_id)
        select_order.status = status
        select_order.save()
        return redirect('order_details', order_id=order_id )
    
    return render(request, 'seller/seller_order/order_details.html', context)


def order_invoice(request, order_id):
    order = Order.objects.get(order_id=order_id)
    orderitems = order.order_item.all()
    context = {'order': order, 'orderitems': orderitems}
    
    template_path = 'seller/seller_order/order_invoice.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# ------------Seller Order List, Order Details And Invoice End-------------


