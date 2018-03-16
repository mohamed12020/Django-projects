from django.shortcuts import render

from .models import Category,Product

from django.contrib.admin.views.main import ChangeList
# Create your views here.

def product_list(request):
    category=None
    theclass = ChangeList
    ords = theclass.sortpro[0]
    categories=Category.objects.all()
    products=Product.objects.filter(available=True).order_by(ords,'name')
    context={'category':category,'categories':categories,'products':products}


    return render(request,'home/products/list.html',context)
