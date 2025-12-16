import django
from django.db import models
from django.utils.text import slugify
# Create your models here.
class ProductBrand(models.Model):
    name=models.CharField(max_length=80)
    class Meta:
        verbose_name='برند'
        verbose_name_plural='برند ها'
    def __str__(self):
        return self.name
class ProductTag(models.Model):
    name=models.CharField(max_length=50, verbose_name="نام تگ")
    is_active=models.BooleanField(default=True, verbose_name="فعال")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="تگ محصول"
        verbose_name_plural="تگ های محصولات"

class ProductCategory(models.Model):
    name=models.CharField(max_length=100, verbose_name="نام دسته بندی")
    image=models.ImageField(upload_to='products/category_images',default='default/category_default.jpg')
    is_active=models.BooleanField(default=True, verbose_name="فعال")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="دسته بندی محصول"
        verbose_name_plural="دسته بندی های محصولات"
        

    
class ProductManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)

class Product(models.Model):
    objects=ProductManager()
    name=models.CharField(max_length=255,verbose_name="نام محصول")
    detail=models.CharField(max_length=500,verbose_name="جزئیات محصول", null=True, blank=True)
    description=models.TextField(verbose_name="توضیحات")
    slug=models.SlugField(max_length=255, verbose_name="اسلاگ",blank=True,null=True,unique=True ,allow_unicode=True)
    image=models.ImageField(upload_to='products/', verbose_name="تصویر محصول", default='default/defaultproduct.jpg')
    description_image=models.ImageField(upload_to='products/description/', verbose_name="تصویر توضیحات محصول",
                                         null=True, blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت")
    brand=models.ForeignKey(ProductBrand,on_delete=models.SET_NULL , null=True,related_name='brands')
    tags=models.ManyToManyField(ProductTag, related_name="tags", verbose_name="تگ ها",null=True, blank=True)
    category=models.ManyToManyField(ProductCategory, related_name="categories", verbose_name="دسته بندی",null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at=models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")
    is_active=models.BooleanField(default=True, verbose_name="فعال")
    is_special=models.BooleanField(default=False,verbose_name='پیشنهاد ویژه ')
    quantity=models.PositiveIntegerField(default=0, verbose_name="موجودی")
    discount_percent=models.PositiveIntegerField(default=0, verbose_name="درصد تخفیف")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="محصول"
        verbose_name_plural="محصولات"
        ordering=['-created_at']
    
    def save(self,*args,**kwargs):
        return super().save(*args,**kwargs)
 


