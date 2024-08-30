from django.shortcuts import render
from  .models import signup_master

# Create your views here.
def signup(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        mobile=request.POST["mobile"]
        password=request.POST["pwd"]
        role_name=request.POST["role_name"]
        ob=signup_master.objects.create(name=name,email=email,mobile=mobile,password=password,role_name=role_name)
        ob.save()
        return render(request,"signup.html",{'output':"register sucess...."})
    return render(request,"signup.html")