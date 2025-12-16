from django import template
from ..models import ProductCategory,ProductBrand,Product
from core.models import BlogPost
from django.db.models import Count, Q
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
def show_special_products(args=5):
    special_product=Product.objects.filter(is_active=True,is_special=True)[:args]
    return {'special_product':special_product}
@register.inclusion_tag('product/discount_products.html')
def show_discount_products(args=5):
    discount_products=Product.objects.filter(is_active=True,discount_percent__gte=0)[:args]
    return {'discount_products':discount_products}
@register.inclusion_tag('product/special_products_home.html')
def show_special_products_home(args=5):
    special_product=Product.objects.filter(is_active=True,is_special=True)[:args]
    return {'special_product':special_product}
@register.inclusion_tag('product/best_categories.html')
def show_best_categories(args=6):
    best_categories=(ProductCategory.objects
                     .filter(is_active=True)
                     .annotate(product_count=Count('categories',filter=Q(categories__is_active=True),distinct=True))
                     .order_by('-product_count'))[:args]
    return {'best_categores':best_categories}
@register.inclusion_tag('product/blog_posts.html')
def show_blog_posts(args=6):
    posts=BlogPost.objects.prefetch_related('tags').active()[:args]
    return {'posts':posts}