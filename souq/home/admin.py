from django.contrib import admin
from .models import Category,Product,Brand

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Brand,BrandAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','Brand','price','stock','available','created','updated']
    list_filter = ['Brand','created','category']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    search_fields = ["name"]
    ordering = ['name']



admin.site.register(Product,ProductAdmin)
