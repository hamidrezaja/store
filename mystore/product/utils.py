import random
from django.utils.text import slugify
def slugify_inctance_name(instance,new_slug=None,save=False):
    if new_slug is not None:
        slug=new_slug
    else:
        slug=slugify(instance.name,allow_unicode=True)
    klass=instance.__class__
    qs=klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        rand_int=random.randint(23000,66000)
        slug=f'{slug}-{rand_int}'
        return slugify_inctance_name(instance,save=save,new_slug=slug)
    instance.slug=slug
    if save:
        instance.save()
    return instance   