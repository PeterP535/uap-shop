from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm, AddToCartForm
from main.models import Item, ShoppingCart, CartItem
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime
from django.http import HttpResponse
from django.core import serializers
from main.models import Item
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import datetime
from django.contrib.auth.forms import UserCreationForm


@login_required(login_url='/login')
def show_main(request):
    product_entries = Item.objects.all()
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    context = {
        'username': request.user.username,
        'product_entries': product_entries,
        'cart_items': cart_items,
        'last_login': request.COOKIES.get('last_login', 'First time login'),
    }

    return render(request, "main.html", context)


@login_required
def add_to_cart_form(request, game_id):
    game = get_object_or_404(Item, id=game_id)  # Get the selected game

    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            
            # Get or create the cart for the logged-in user
            cart, created = ShoppingCart.objects.get_or_create(user=request.user)
            
            # Check if the game is already in the cart
            cart_item, created = CartItem.objects.get_or_create(cart=cart, item=game)
            
            if not created:
                cart_item.quantity += amount  # If already in the cart, increment quantity
            else:
                cart_item.quantity = amount
            cart_item.save()

            return HttpResponseRedirect(reverse('main:show_main'))
    else:
        form = AddToCartForm()

    context = {
        'game': game,
        'form': form,
    }
    
    return render(request, 'add_to_cart_form.html', context)


@login_required
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required
def edit_product(request, game_id):
    game = get_object_or_404(Item, id=game_id)
    form = ProductForm(request.POST or None, instance=game)
    
    if form.is_valid():
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form, 'game': game}
    return render(request, 'create_product.html', context)

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Item, id=product_id)
    product.delete()
    return redirect('main:show_main')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:login')
    return render(request, 'register.html', {'form': form})


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             response = HttpResponseRedirect(reverse('main:show_main'))
#             response.set_cookie('last_login', str(datetime.datetime.now()))
#             return response
#     return render(request, 'login.html')

# def logout_view(request):
#     logout(request)
#     response = HttpResponseRedirect(reverse('main:login'))
#     response.delete_cookie('last_login')
#     return response

# Login view
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', str(datetime.datetime.now()))  # Store last login time in a cookie
            return response
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    context = {'form': form}
    return render(request, 'login.html', context)

# Logout view
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')  # Optionally delete the last login cookie
    return response






@login_required
def edit_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    
    # Check if the item belongs to the user's cart
    if cart_item.cart.user != request.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = AddToCartForm(request.POST, instance=cart_item)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = AddToCartForm(instance=cart_item)

    context = {
        'form': form,
        'cart_item': cart_item,
    }
    return render(request, 'edit_cart_item.html', context)

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Item, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'edit_product.html', context)

@login_required
def delete_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('main:show_main')

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# View to display all items in JSON format
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# View to display an item by its ID in XML format
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# View to display an item by its ID in JSON format
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
