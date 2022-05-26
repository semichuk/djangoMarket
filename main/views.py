from django.shortcuts import render, redirect
from .models import Favorite
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
import sqlite3
from .userRegistrationExtended import UserRegistrationEntended
from .SELECT_FROM_DB import select_from_db
# Create your views here.


def discription(request):
    id_get = request.GET.get('id')
    id = Product.objects.filter(id=id_get).values('id')
    name = Product.objects.filter(id=id_get).values('name')
    cost = Product.objects.filter(id=id_get).values('cost')
    description = Product.objects.filter(id=id_get).values('description')
    image = Product.objects.filter(id=id_get).values('image')
    id_ = id[0]
    id__ = id_['id']
    name_ = name[0]
    name__ = name_['name']
    cost_ = cost[0]
    cost__ = cost_['cost']
    description_ = description[0]
    description__ = description_['description']
    image_ = image[0]
    image__ = image_['image']
    obje = Product.objects.filter(id=id_get).all()
    costs = obje.cost
    print(costs)
    return render(
        request, 'main/discription.html',
        {'name': name__, 'cost': cost__, 'image': image__,
         'description': description__})


def registration(request):
    if request.method == "POST":
        form = UserRegistrationEntended(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
            messages.success(request, f'Account created for {username}')
        else:
            username = form.cleaned_data.get('username')
            return render(request, 'main/registration.html', {'form': form})
    else:
        form = UserRegistrationEntended()
        return render(request, 'main/registration.html', {'form': form})


def home(request):
    favorites = Favorite.objects.all()
    print(request.user)
    return render(
        request, 'main/home.html',
        {'title': 'Home', 'favorites': favorites})


def about(request):
    return render(request, 'main/about.html')


def catalog(request):
    products = Product.objects.all()
    return render(
        request, 'main/catalog.html',
        {'products': products})


def user_data(request):
    return render(request, 'main/user.html')


@csrf_exempt
def user_data_applying(request):
    if request.POST:

        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()

        name = request.POST["name"]
        surname = request.POST["surname"]
        numberPhone = request.POST["numberPhone"]
        userEmail = request.POST["userEmail"]
        country = request.POST["country"]

        cursor.execute(
            f"INSERT INTO main.main_user VALUES (NULL, '{name}','{surname}','{numberPhone}','{userEmail}','{country}')")
        connection.commit()
        connection.close()

        return HttpResponse('ok')


def purchase_confirmation(request):
    connection = sqlite3.connect('db.sqlite3')
    query = f"SELECT * FROM main.auth_user WHERE username LIKE '{request.user}';"
    user  = select_from_db(connection, query)
    id = request.GET.get('id')
    query = f"SELECT * FROM main.main_product WHERE id={request.GET.get('id')};"
    product = select_from_db(connection, query)
    connection.commit()
    connection.close()

    return render(request, 'main/purchase_confirmation.html')

# def sign_in(request):
  #  return render(request, 'main/sign_in.html')
