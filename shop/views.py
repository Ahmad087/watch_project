from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import ListView
from django.contrib.auth.models import Group, User
from .forms import SignUpForm
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request = request,
                  template_name = "shop/home.html")

def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form':form})

def signinView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('product_list')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/signin.html', {'form':form})

def signoutView(request):
    logout(request)
    return redirect('signin')
 
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
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                  'cart_product_form': cart_product_form})