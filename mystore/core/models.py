from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')
    def popular_posts(self):
        return self.get_queryset().order_by('-counter_view')[:5]
class BlogPost(models.Model):
    objects=BlogPostManager()
    title=models.CharField(max_length=200,verbose_name="عنوان")
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="نویسنده")
    content=models.TextField(verbose_name="محتوا")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    updated_at=models.DateTimeField(auto_now=True,verbose_name="تاریخ بروزرسانی")
    image=models.ImageField(upload_to='blog_images/',verbose_name="تصویر",null=True,blank=True)
    counter_view=models.PositiveIntegerField(default=0,verbose_name="تعداد بازدید")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="پست وبلاگ"
        verbose_name_plural="پست‌های وبلاگ"
        ordering=['-created_at']
class blogCategory(models.Model):
    name=models.CharField(max_length=50,verbose_name="نام دسته‌بندی")
    posts=models.ManyToManyField(BlogPost,related_name='categories',verbose_name="پست‌ها",blank=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="دسته‌بندی وبلاگ"
        verbose_name_plural="دسته‌بندی‌های وبلاگ"
class BlogTag(models.Model):
    name=models.CharField(max_length=50,verbose_name="نام برچسب")
    posts=models.ManyToManyField(BlogPost,related_name='tags',verbose_name="پست‌ها",blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="برچسب وبلاگ"
        verbose_name_plural="برچسب‌های وبلاگ"
class BlogCommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')
    def post_comments(self,post):
        return self.get_queryset().filter(post=post,admin_reviewed=True)
class BlogComment(models.Model):
    objects=BlogCommentManager()
    post=models.ForeignKey(BlogPost,on_delete=models.CASCADE,verbose_name="پست",related_name="comments")
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر")
    comment_content=models.TextField(verbose_name="محتوا")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    admin_reviewed=models.BooleanField(default=False,verbose_name="بررسی شده توسط مدیر")

    def __str__(self):
        return f"نظر {self.user.username} در مورد {self.post.title}"
    class Meta:
        verbose_name="نظر وبلاگ"
        verbose_name_plural="نظرات وبلاگ"
        ordering=['-created_at']

        

