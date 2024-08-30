from django.shortcuts import render
from signup.models import signup_master
from change_profile.models import profile_master

# Create your views here.
def pprofile(request):
    email = request.session.get('email')
    
    if email:
        obj = signup_master.objects.get(email=email)  
        ob = profile_master.objects.filter(email=email)
        return render(request, 'pprofile.html', {'data': ob, 'data1': obj})
    else:
        return render(request, 'pprofile.html', {'error': 'No email found in session'})

def phome(request):
    name=request.session.get('name')
    obj=signup_master.objects.get(name=name)
    return render(request,"phome.html",{'name':name,'data':obj})