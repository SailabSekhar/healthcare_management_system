from django.shortcuts import render,redirect
from signup.models  import signup_master

# Create your views here.
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('dashboard')  

def login (request):
    if request.method=="POST":
        email=request.POST["email"]
        pwd=request.POST["pwd"]
        try:
            ob=signup_master.objects.get(email=email,password=pwd)
            request.session['name']=ob.name
            request.session['email']=ob.email
            request.session['mobile']=ob.mobile
            request.session['role_nmae']=ob.role_name

            if ob.role_name=="doctor":
                return redirect("dhome")
            elif ob.role_name=="patient":
                return redirect('phome')
            elif ob.role_name=="admin":
                return redirect("ahome")
            else:
                return render(request,"login.html")
        except Exception as e:
            return render(request,"login.html",{"data":"invalid" +  str(e)})

    return render(request,"login.html")
