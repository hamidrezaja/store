from django.contrib import admin
from .models import BlogPost, BlogTag, BlogComment ,blogCategory  
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','user', 'created_at', 'updated_at')

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('post','user', 'created_at', 'admin_reviewed')
    
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogTag)
admin.site.register(BlogComment, BlogCommentAdmin)
admin.site.register(blogCategory)