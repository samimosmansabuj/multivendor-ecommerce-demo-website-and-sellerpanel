from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Customer, Seller
from order.models import Order
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from xhtml2pdf import pisa
from django.template.loader import get_template
import uuid
from django.contrib.auth.decorators import login_required
import random

# Create your views here.
@login_required(login_url='login')
def download_invoice(request, order_id):
    if request.user.is_customer == False:
        return redirect('login')
    
    order = Order.objects.get(order_id=order_id)
    orderitems = order.order_item.all()
    context = {'order': order, 'orderitems': orderitems}
    
    template_path = 'account/my_account/invoice.html'
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    
    # return render(request, 'account/my_account/invoice.html', context)



@login_required(login_url='login')
def view_order(request, order_id):
    if request.user.is_customer == False:
        return redirect('login')
    
    order = Order.objects.get(order_id=order_id)
    orderitems = order.order_item.all()
    context = {'order': order, 'orderitems': orderitems}
    return render(request, 'account/my_account/view_order.html', context)


@login_required(login_url='login')
def my_account(request):
    if request.user.is_customer == False:
        return redirect('login')
    print(request.user.is_customer)
    customer = request.user
    orders = Order.objects.filter(customer=customer)
    context = {'orders': orders}
    
    return render(request, 'account/my_account/my_account.html', context)

@login_required(login_url='login')
def Logout(request):
    # if request.user.is_customer == False:
    #     return redirect('login')
    logout(request)
    return redirect('login')



def Login(request):
    if request.user.is_authenticated:
        user = request.user
        if Customer.objects.filter(username=user).exists():
            return redirect('my_account')
        else:
            return render(request, 'account/login.html')
    
    if request.method == 'POST':
        logout(request)
        username = request.POST['username']
        password = request.POST['password']
        if not Customer.objects.filter(username=username).exists():
            messages.warning(request, "This is not a customer account!")
            return redirect(request.META['HTTP_REFERER'])
        else:
            customer = Customer.objects.get(username=username)
            context = {}
            if not customer:
                context['wrong_user'] = "Invalid Username!"
            else:
                user = authenticate(username=username, password=password)
                if not user:
                    wrong_pass = "Wrong Password!"
                    context['wrong_pass'] = wrong_pass
                else:
                    login(request, user)
                    return redirect('my_account')
        
    return render(request, 'account/login.html')





# Registration Section Start----------------------
def Registration(request):
    if request.user.is_authenticated:
        user = request.user
        if Customer.objects.filter(username=user).exists():
            return redirect('my_account')
        else:
            return render(request, 'account/registration.html')
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        auth_token = uuid.uuid4()
        otp_token = random.randint(111111, 999999)
        
        customer = Customer.objects.create(
            username=username, first_name=first_name, last_name=last_name, phone_number=phone_number, email=email, auth_token=auth_token, otp_token=otp_token
        )
        customer.set_password(password)
        customer.is_customer = True
        customer.is_verified = False
        customer.save()
        send_mail_registration(email, auth_token, otp_token)
        
        return redirect('registration_verification', id=customer.id)
        
    return render(request, 'account/registration.html')

def send_mail_registration(email, auth_token, otp_token):
    subject = 'Your Safa World Shop Customer Account Verification Mail!'
    message = f'''Dear User,
    Your Registration Verification OTP is :{otp_token}
    or
    Click this link for verify complete your account: http://127.0.0.1:8000/account/verify-registration-link/{auth_token}'''
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

def verify(request, auth_token):
    if request.user.is_authenticated:
        return redirect('my_account')
    
    customer = Customer.objects.get(auth_token=auth_token)
    if customer:
        customer.is_verified = True
        customer.auth_token = None
        customer.otp_token = None
        customer.save()
        messages.success(request, "Accouint Verification Complete Successfully!")
        return redirect('login')
    else:
        messages.success(request, "Your Account Verification Failed!")
        return redirect('login')

def registration_verification(request, id):
    if request.user.is_authenticated:
        return redirect('my_account')
    
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        otp_token = request.POST['otp_token']
        if customer.otp_token == otp_token:
            customer.is_verified = True
            customer.auth_token = None
            customer.otp_token = None
            customer.save()
            messages.success(request, "Accouint Verification Complete Successfully!")
            return redirect('login')
        else:
            messages.success(request, "OTP Incorrect!")
    
    return render(request, 'account/reg_verification.html', {'customer': customer})
# Registration Section End----------------------

