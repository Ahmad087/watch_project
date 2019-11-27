from django.urls import path
from .views import (
    ItemDetailView,
    checkout,
    home,
    HomeView
)

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product')
    
]