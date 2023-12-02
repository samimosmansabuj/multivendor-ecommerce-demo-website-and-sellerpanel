from django.shortcuts import render
from .models import Product, Category, Sub_Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

# Create your views here.
def products(request):
    categories = Category.objects.all()
    
    price_filter = request.GET.get('filter')
    
    if price_filter:
        if price_filter == 'low':
            all_product = Product.objects.order_by('discount_price')
            
            item_page_page = 2
            paginator = Paginator(all_product, item_page_page)
            page = request.GET.get('page')
            try:
                products = paginator.page(page)
            except PageNotAnInteger:
                products = paginator.page(1)
            except EmptyPage:
                products = paginator.page(1)
            except InvalidPage:
                products = paginator.page(1)
            context = {'categories': categories, 'products': products, 'paginator': paginator, 'item_page_page': item_page_page}
            return render(request, 'product/product.html', context)
    
    
        elif price_filter == 'high':
            all_product = Product.objects.order_by('-discount_price')
            
            item_page_page = 2
            paginator = Paginator(all_product, item_page_page)
            page = request.GET.get('page')
            try:
                products = paginator.page(page)
            except PageNotAnInteger:
                products = paginator.page(1)
            except EmptyPage:
                products = paginator.page(1)
            except InvalidPage:
                products = paginator.page(1)
            context = {'categories': categories, 'products': products, 'paginator': paginator, 'item_page_page': item_page_page}
            return render(request, 'product/product.html', context)
    
    
    
    else:
        all_product = Product.objects.all()
    
        item_page_page = 2
        paginator = Paginator(all_product, item_page_page)
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(1)
        except InvalidPage:
            products = paginator.page(1)
        context = {'categories': categories, 'products': products, 'paginator': paginator, 'item_page_page': item_page_page}
        return render(request, 'product/product.html', context)




def category_product(request, id):
    cat = Category.objects.get(id=id)
    products = Product.objects.filter(category=cat)
    categories = Category.objects.all()
    context = {'products': products, 'categories': categories}
    
    return render(request, 'product/product.html', context)



def product_details(request, slug):
    product = Product.objects.get(product_slug=slug)
    cat = product.category
    related_products = Product.objects.filter(category=cat)

    context = {'product': product, 'related_products': related_products}
    return render(request, 'product/product_details.html', context)