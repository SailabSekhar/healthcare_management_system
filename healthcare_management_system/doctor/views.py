from django.shortcuts import render
from signup.models import signup_master
from change_profile.models import profile_master

# Create your views here.
def dprofile(request):
   
    email = request.session.get('email')
    
    if email:
        obj = signup_master.objects.get(email=email)  
        ob = profile_master.objects.filter(email=email)
        return render(request, 'dviewprofile.html', {'data': ob, 'data1': obj})
    else:
        return render(request, 'dviewprofile.html', {'error': 'No email found in session'})
def dview(request):
    name=request.session.get('name')
    ob=signup_master.objects.get(name=name)
    obj=signup_master.objects.filter(role_name='patient')
    return render(request,'dview.html',{'user':ob,'data1':obj,'user':ob})
def dhome(request):
    name=request.session.get('name')
    return render(request,"dhome.html",{'name':name})