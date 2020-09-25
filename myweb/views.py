from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

ALL_Username = []
ALL_Password = []
ALL_Email = []

# Create your views here.
def index(req):
    G = GroupManager.objects.all()
    U = User.objects.all()
    print(req.user.is_authenticated)
    if req.user.is_authenticated:
        return render(req, r'myweb/In_Login.html', {'Story':G})
    else:
        return render(req ,r'myweb/index.html', {'Story':G})

def newtheme(req):
    return render(req ,r'myweb/newtheme.html')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def register(req):
    return render(req ,r'myweb/register.html')

def login_Web(req):
    return render(req ,r'myweb/Login.html')

def reg_success(req):
    ALL_Username.clear();
    ALL_Email.clear();
    for i in User.objects.all():
        ALL_Username.append(i.username)
        ALL_Email.append(i.email)
    if req.method =="POST":
        G = GroupManager()
        if req.POST.get('username') not in ALL_Username or req.POST.get('email') not in ALL_Email:
            user = User.objects.create_user(username = req.POST.get('username'), password = req.POST.get('password'), email = req.POST.get('email'))
            G.Phone = req.POST.get('phone')
            G.Nickname = req.POST.get('nickname')
            G.save()
            user.save()
            return redirect('/')
        else: return render(req ,r'myweb/register.html')
    else:
        return render(req ,r'myweb/register.html')

def log_in(req):
    if req.method =="POST":
        Username = req.POST.get("username")
        Password = req.POST.get("password")
        user = authenticate(username=Username, password=Password)
        if user is not None:
            if user.is_active:
                req.session.set_expiry(3600) #sets the exp. value of the session
                login(req, user)
                return redirect("/")
        else:

            return render(req,r"myweb/login.html",{"Feil":"Username or Password is incorrect"})

def log_out(req):
    logout(req)
    return redirect('/')