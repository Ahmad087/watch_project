from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('shop/product/list', views.product_list, name='product_list'),
    path("shop/home", views.home, name="home"),
    path("shop/register", views.register, name="register"),
    path('<slug:category_slug>/', views.product_list, 
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]