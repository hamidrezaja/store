from django.contrib import admin
from .models import Product,ProductTag,ProductCategory,ProductBrand
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'quantity', 'created_at', 'updated_at','slug')
    search_fields = ('name', 'detail', 'description')
    list_filter = ('is_active', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    verbose_name = "محصول"
    verbose_name_plural = "محصولات"

admin.site.register(Product, ProductAdmin)

class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)
    ordering = ('name',)
    verbose_name = "تگ محصول"
    verbose_name_plural = "تگ های محصولات"

admin.site.register(ProductTag, ProductTagAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)
    ordering = ('name',)
    verbose_name = "دسته بندی محصول"
    verbose_name_plural = "دسته بندی های محصولات"

admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductBrand)