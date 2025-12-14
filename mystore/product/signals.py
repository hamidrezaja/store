from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .utils import slugify_inctance_name
from .models import Product
@receiver(pre_save,sender=Product)
def product_pre_save(sender,instance,*args, **kwargs):
    if not instance.slug :
        slugify_inctance_name(instance,save=False)
        
