from django import template
from ..models import ProductCategory,ProductBrand,Product
register = template.Library()


@register.inclusion_tag("product/product_category.html")
def show_product_categories():
    categories = ProductCategory.objects.filter(is_active=True)
    return {'categories': categories}
@register.inclusion_tag('product/product_brand.html')
def show_product_brands():
    brands=ProductBrand.objects.all()
    return {'brands':brands}
@register.inclusion_tag('product/special_product.html')
def show_special_products():
    special_product=Product.objects.filter(is_active=True,is_special=True)[:1]
    return {'special_product':special_product}