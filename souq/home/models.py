from django.db import models




# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,unique=True)
    # SeeFirst = models.PositiveIntegerField(default=0)


    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return  self.name



class Brand(models.Model):
    Category=models.ForeignKey(Category,related_name='Brands',on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,unique=True)


    class Meta:
        ordering=('name',)
        verbose_name='Brand'
        verbose_name_plural='Brands'

    def __str__(self):
        return  self.name
class Product(models.Model):

    category=models.ForeignKey(Category,related_name='products',on_delete=models.DO_NOTHING)
    Brand=models.ForeignKey(Brand,related_name='products',on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    see_first = models.PositiveIntegerField(default=0)#zero =in normal sort

    class Meta:
        ordering=('name',)
        index_together=(('id','slug'),)
    def __str__(self):
        return self.name

