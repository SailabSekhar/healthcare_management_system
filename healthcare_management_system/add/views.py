from django.shortcuts import render

# Create your views here.
def add(request):
    if request.method=="POST":
        a=int(request.POST["fno"])
        b=int(request.POST["sno"])
        result=a+b
        return render(request,"add.html",{"output":result})

    return render(request,"add.html")
