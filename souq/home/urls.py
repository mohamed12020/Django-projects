from django.urls import re_path
from .views import product_list

urlpatterns=[

    re_path(r'^$',product_list,name='product_list'),


]