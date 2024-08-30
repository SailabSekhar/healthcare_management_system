from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def  contact(request):
    return render(request,"contact.html")
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")

def home(request):
    return HttpResponse("<h1>welcome to home ...</h1>")
