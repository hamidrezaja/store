from django.contrib import admin
from .models import BlogPost, BlogTag, BlogComment ,blogCategory  
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class BlogPostAdmin(SummernoteModelAdmin):
    list_display = ('title','user', 'created_at', 'updated_at')
    summernote_fields = '__all__'
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('post','user', 'created_at', 'admin_reviewed')
    
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogTag)
admin.site.register(BlogComment, BlogCommentAdmin)
admin.site.register(blogCategory)