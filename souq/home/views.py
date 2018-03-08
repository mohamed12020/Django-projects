from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Category,Product

# Create your views here.

def product_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    products=Product.objects.filter(available=True,see_first=0)
    see_first_products=Product.objects.filter(available=True,see_first__gt=0).order_by("see_first")
    context={'category':category,'categories':categories,'products':products,'see_first_products':see_first_products}
    # if category_slug:
    #     category=get_object_or_404(Category,slug=category_slug)
    #     products=products.filter(category=category)

    return render(request,'home/products/list.html',context)
