from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone




from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse










# Create your views here.
# def show_main(request):
#     product_entries = Item.objects.all()


#     context = {
#         'npm' : '2306152361',
#         'nama': 'Peter Putra Lesmana',
#         'class': 'PBP B',
#         'product_entries': product_entries,
#     }

#     return render(request, "main.html", context)

# Show main view with user info and last login from cookies
def show_main(request):
    product_entries = Item.objects.all()
    
    # Check if user is logged in
    if request.user.is_authenticated:
        username = request.user.username
        last_login = request.COOKIES.get('last_login', 'First time login')

        context = {
            'username': username,
            'last_login': last_login,
            'product_entries': product_entries,
        }
    else:
        context = {
            'product_entries': product_entries,
        }

    response = render(request, "main.html", context)
    
    # Set the last login cookie if the user is authenticated
    if request.user.is_authenticated:
        response.set_cookie('last_login', timezone.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    return response

# Registration view
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            return redirect('main:login')
    return render(request, 'register.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
    return render(request, 'login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('main:login')


def create_product(request):

    # if form.is_valid() and request.method == "POST":
    #     form.save()
    #     # product = form.save(commit=False)
    #     # product.user = request.user
    #     # product.save()
    #     return redirect('main:show_main')

    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user  # Link product to logged-in user
        product.save()
        return redirect('main')

    context = {'form': form}
    return render(request, "create_product.html", context)



def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")