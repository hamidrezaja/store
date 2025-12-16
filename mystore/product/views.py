from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.



def product_list(request,**kwargs):
    products = Product.objects.all()
    if kwargs.get('category'):
        products=products.filter(category__name=kwargs.get('category'))
    if kwargs.get('brand'):
        products=products.filter(brand__name=kwargs.get('brand'))
    if kwargs.get('special'):
        products=products.filter(is_special=True)
    paginator = Paginator(products, 10)  
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    context = {'page_obj': products}
    return render(request, 'product/product_list.html', context)

def product_detail(request, **kwargs):
    product_id = kwargs.get('pk')
    product_name=kwargs.get('slug')
    product = Product.objects.all().get(id=product_id)
    product_tags = product.tags.all()
    product_categories = product.category.all()

    context = { 'product': product,
                'product_tags': product_tags,
                'product_categories': product_categories }
    return render(request, 'product/product_detail.html', context)

def search(request,**kwargs):
    search_bar=request.GET.get('searchbar')
    products=Product.objects.filter(name__icontains=search_bar).distinct()
    print(products)
    context={'page_obj':products}
    return render(request,'product/product_list.html',context)