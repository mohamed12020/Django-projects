from django.shortcuts import render

from .models import Category,Product

from django.contrib.admin.views.main import ChangeList
# Create your views here.

def product_list(request):
    category=None
    theclass = ChangeList
    ords = theclass.sortpro[0]
    categories=Category.objects.all()
    products=Product.objects.filter(available=True,see_first=0).order_by(ords,'name')
    see_first_products=Product.objects.filter(available=True,see_first__gt=0).order_by("see_first")
    context={'category':category,'categories':categories,'products':products,'see_first_products':see_first_products}


    return render(request,'home/products/list.html',context)
