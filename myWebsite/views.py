from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from django.core.exceptions import PermissionDenied
from .models import tb_house

# Create your views here.
def index(req): 
    contentHouse = tb_house.objects.all().order_by("id")
    data = {
        'content': contentHouse
    }
    return render(req, "index.html",data)
    # return render(req,"index.html")
# def home(req):
#     return render(req,"home.html")

@login_required(login_url="/login")
def product(req):
    content = tb_house.objects.all()
    data = {
        "contentHouse": content,
    }
    return render(req,"product.html",data)

@login_required(login_url="/login")
@permission_required("is_staff", login_url="/loginWarning")
def addProduct(req):
    return render(req,"addProduct.html")

def recordHouse(req):
    name = req.POST["name_house"]
    price = req.POST["price_house"]
    address = req.POST["address_house"]
    detail = req.POST["detail_house"]
    photo = req.FILES["photo_house"]
    # print(photo)
    content = tb_house(name_house=name, price_house = price, address_house=address, detail_house=detail, status_house=True, photo_house=photo)
    content.save()
    return redirect("/manageProduct")

def editHouse(req):
    id = req.POST["id"]
    name = req.POST["name_house"]
    price = req.POST["price_house"]
    address = req.POST["address_house"]
    detail = req.POST["detail_house"]
    try:
        photo = req.FILES["photo_house"]
    except KeyError:
        photo = None
    content = tb_house.objects.get(pk=id)
    content.name_house = name
    content.price_house = price
    content.address_house = address
    content.detail_house = detail
    if photo is not None:
        os.remove("media/"+str(content.photo_house))
        content.photo_house = photo
    content.save()
    return redirect("/manageProduct")

@login_required(login_url="/login")
@permission_required("is_staff", login_url="/loginWarning")
def manageProduct(req):
    content = tb_house.objects.all()
    data = {
        "contentHouse": content,
    }
    return render(req,"manageProduct.html",data)

#Delete product
def deleteHouse(req):
    id = req.POST["id"]
    content = tb_house.objects.get(pk=id)
    content.delete()
    return redirect("/manageProduct")

def manageAccount(req):
    print(User.get_username())
    content = []
    data = {
        "contentAccount": content,
    }
    return render(req,"manageAccount.html",data)

def login(req):
    if req.user.is_authenticated:
        return redirect("/")
    return render(req, "login.html")

def loginMethod(req):
    username = req.POST["username"]
    password = req.POST["password"]
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(req, user)
        return redirect('/')
    else:
        messages.error(req, "Login Failed")
        return redirect("/login")
def logoutMethod(req):
    auth.logout(req)
    return redirect("/login")

def register(req):
    return render(req,"register.html")

def registMethod(req):
    fname = req.POST["fname"]
    lname = req.POST["lname"]
    email = req.POST["email"]
    username = req.POST["username"]
    password = req.POST["password"]
    repassword = req.POST["repassword"]
    if password == repassword:
        if User.objects.filter(username = username).exists():
            messages.error(req,"Username has been used")
        elif User.objects.filter(email=email).exists():
            messages.error(req,"Email has been used")
        else:
            user = User.objects.create_user(
                first_name = fname,
                last_name = lname,
                username = username,
                password = password,
                email = email,
            )
            user.save()
            # messages.error(req,"Data saved")
    else:
        messages.error(req,"password is not equal to re-password")
    user.save()
    return redirect("/login")

def loginWarning(req):
    return render(req,"loginWarning.html")


def handler404(req, exception):
    return render(req,"404errorPage.html")
def handler500(req):
    return render(req,"500errorPage.html",status=500)
def handler403(req, exception):
    return render(req, "403errorPage.html")
def handler400(req, exception):
    return render(req, "400errorPage.html")