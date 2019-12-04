from django.urls import path
from . import views
from django.conf import settings


app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
   #path('shop/product/list', views.product_list, name='product_list'),
    path('account/create/', views.signupView, name='signup'),
    path("shop/home", views.home, name="home"),
    path('<slug:category_slug>/', views.product_list, 
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]