from django import template
from ..models import blogCategory,BlogPost
import jdatetime
register = template.Library()


@register.inclusion_tag('core/blog_left_sidebar.html')
def blog_left_side():
    categories=blogCategory.objects.all()
    favorite_posts=BlogPost.objects.popular_posts().active()
    context={
        'category':categories,
        'favorite_posts':favorite_posts
    }
    return context

@register.filter
def jalali_time(value,format='%Y/%m/%d'):
    if not value:
         return ''
    if hasattr(value,'date'):
        value=value.date()
    return jdatetime.date.fromgregorian(date=value).strftime(format)
    
    