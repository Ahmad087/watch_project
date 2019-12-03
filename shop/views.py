from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView


def base(request):
    return render(request = request,
                  template_name = "shop/base.html")

def register(request):
    form = UserCreationForm
    return render(request = request,
                  template_name = "shop/register.html",
                  context={"form":form})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})
