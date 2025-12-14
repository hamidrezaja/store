from django.urls import path
from . import views
urlpatterns = [
    path('product-list/', views.product_list, name='product_list'),
    path('product-list/category/<str:category>/', views.product_list, name='product_list_by_category'),
    path('product-list/brand/<str:brand>',views.product_list,name='product_brand'),
    path('product-detail/<int:pk>/<str:slug>', views.product_detail, name='product_detail'),
    path('product/search',views.search,name='search')

]
