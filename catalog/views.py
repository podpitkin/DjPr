from django.shortcuts import render

from catalog.models import Product


def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

def catalog_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request,'prod_list.html', context)

def prod_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, 'prod_detail.html', context)

