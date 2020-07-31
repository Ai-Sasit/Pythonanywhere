from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
	#return HttpResponse('ยินดีต้อนรับ เข้าสู่เว็บไซต'+req.method)
    return render(req ,r'myweb/index.html')

def newtheme(req):
    return render(req ,r'myweb/newtheme.html')

def detail(req, question_id):
    return render(req ,r"myweb/detail.html")

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)