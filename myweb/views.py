from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from datetime import datetime
ALL_Username = []
ALL_Password = []
ALL_Email = []
ALL_Author = []
Author_status = bool()
Writer_button = bool()
Story_Type = None
search_key = None

def index(req):
    global Writer_button
    global Author_status
    global search_key
    global Story_Type
    if Story_Type is not None:
        G = StoryElements.objects.filter(Story_Type = Story_Type).order_by('-Date_Created')
        Story_Type = None
    elif search_key is not None:
        G = StoryElements.objects.filter(StoryName__contains=search_key).order_by('-Date_Created')
        search_key = None
    else:
        G = StoryElements.objects.all().order_by('-Date_Created')
    if req.user.is_superuser:
        return render(req, r'myweb/AdminLogin.html', {'Story':G})
    elif req.user.is_authenticated:
        if (Writer_button is True and Author_status is False):
            Writer_button = False; Author_status = True
            return render(req, r'myweb/In_Login.html',{'Story':G,'Fail':"You must be add Author name in Author setting!",'status':'true'})
        else:
            return render(req, r'myweb/In_Login.html', {'Story':G})
    else:
        return render(req ,r'myweb/index.html', {'Story':G})

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
            G.User = User.objects.get(username = req.POST.get('username'))
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
                req.session.set_expiry(3600)
                login(req, user)
                return redirect("/")
        else:

            return render(req,r"myweb/login.html",{"Feil":"Username or Password is incorrect"})

def log_out(req):
    logout(req)
    return redirect('/')


def Editpro(req):
    G= GroupManager.objects.filter(User=req.user.id)
    Username = req.user.username
    Email = req.user.email
    phone = G[0].Phone
    Nickname = G[0].Nickname
    return render(req ,r'myweb/EditProfile.html',{"User":f"{Username}","Email":Email,"Phone":f"{phone}","Nickname":Nickname})

def Edit_Process(req):
    G = GroupManager.objects.get(User=req.user.id)
    U = User.objects.get(id=req.user.id)
    U.username = req.POST.get("username")
    U.email = req.POST.get("email")
    G.Phone = req.POST.get("phone")
    G.Nickname = req.POST.get("nickname")
    U.save()
    G.save()
    return redirect("/")

def AuthorEdit(req):
    try:
        W = Writer.objects.filter(GID = GroupManager.objects.get(User=req.user.id))
        Author_name = W[0].Name
        Author_bio = W[0].BIO
        return render(req ,r'myweb/AuthorEdit.html', {'Name':f"{Author_name}", 'bio':f"{Author_bio}",'change':"Edit"})
    except:
        return render(req,r'myweb/AuthorEdit.html',{'change':"Add"})

def AuthorX(req):
    ALL_Author.clear()
    for author in Writer.objects.all():
        ALL_Author.append(author.Name)
    if req.method == "POST":
        if req.POST.get("author") not in ALL_Author:
            Author_name = req.POST.get("author")
        else:
            try:
                Writer.objects.get(GID = GroupManager.objects.get(User=req.user.id))
                return render(req,r"myweb/AuthorEdit.html",{'color_fail':'rgb(255, 0, 0)','change':"Edit"})
            except:
                return render(req,r"myweb/AuthorEdit.html",{'color_fail':'rgb(255, 0, 0)','change':"Add"})
        Bio = req.POST.get("Bio")
        W = Writer()
        W.GID = GroupManager.objects.get(User=req.user.id)
        W.Name = Author_name
        W.BIO = Bio
        W.save()
        return redirect('/')

def Writing(req):
    global Author_status
    global Writer_button
    try:
        Writer.objects.get(GID = GroupManager.objects.get(User=req.user.id))
        return render(req,r"myweb/Writer.html")
    except:
        Writer_button = True
        Author_status = False
        return redirect('/')

def WritingX(req):
    SE = StoryElements()
    S = Story()
    if req.method =="POST":
        SE.WID = Writer.objects.get(GID = GroupManager.objects.get(User=req.user.id))
        SE.StoryName = req.POST.get('StoryName')
        SE.Story_Type = req.POST.get('Type')
        SE.AutoDate = datetime.now().strftime("%d/%m/%Y %H:%M")
        SE.save()
        Test = StoryElements.objects.filter(WID =  Writer.objects.get(GID = GroupManager.objects.get(User=req.user.id)))
        S.StoryID = Test[len(Test)-1]
        S.Story_Article = req.POST.get('description')
        S.save()

    return redirect('/')

def Reading(req,index):
    SE = StoryElements.objects.filter(SID = index)
    S = Story.objects.filter(StoryID = index)
    NameStory = SE[0].StoryName
    DateStory = SE[0].AutoDate
    ContentStory = S[0].Story_Article
    return render(req,r"myweb/Read.html",{"Title_Name":f"{NameStory}","Date":f"{DateStory}","Content":f"{ContentStory}"})

def Type(req,type_select):
    global Story_Type
    if type_select =='Emotion': Story_Type = "Emotion"
    elif type_select == "Short": Story_Type = "Short"
    elif type_select == "Exper": Story_Type = "Experience"
    elif type_select == "Love": Story_Type = "Love"
    elif type_select == "Com": Story_Type = "Comedy"
    else: Story_Type = None
    return redirect('/')

def Search(req):
    global search_key
    if req.method =="POST": search_key = req.POST.get("Key")
    return redirect("/")