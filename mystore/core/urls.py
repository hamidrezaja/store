from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home_page,name='home'),
    path('about/',views.about_us,name='about'),
    path('contact/',views.contact_us,name='contact'),
    path('faq/',views.faq_page,name='faq'),
    path('blog/',views.blog_page,name='blog'),
    path('blog/search/', views.search_blog, name='search-blog'),
    path('blog/category/<str:category_name>/', views.category_blog, name='category_blog'),
    path('blog-details/<int:id>/',views.blog_details_page,name='blog-details'),
    path('login/',views.login_page,name='login'),
    path('register/',views.register_page,name='register'),
]
