from django.shortcuts import render,redirect
from signup.models  import signup_master
from change_profile.models import profile_master
def update(request):
    signup_obj = signup_master.objects.get(email=email)
    profile_objs = profile_master.objects.filter(email=signup_obj)
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
         
        mobile=request.POST['mobile']
        role_name=request.POST['role_name']
        ob=signup_master.objects.filter(email=email).update(name=name,mobile=mobile,role_name=role_name)
        return redirect('aviewdata')
    return render(request,'aviewdata.html')


def aviewdata(request):
    signup_data = signup_master.objects.all()
    combined_data = []
    for signup in signup_data:
        profile = profile_master.objects.filter(email=signup)
        combined_data.append({
            'signup': signup,
            'profile': profile
        })
    
    if request.method == "POST":
        btn = request.POST['btn']
        email = request.POST['email']
        if btn == 'edit':
            signup_obj = signup_master.objects.get(email=email)
            return render(request, 'edit.html', {'data1': signup_obj})
        elif btn == 'delete':
            signup_master.objects.get(email=email).delete()
            return redirect('aviewdata')
    
    return render(request, 'aviewdata.html', {'data': combined_data})


def ahome(request):
    name=request.session.get('name')
    return render(request,"ahome.html",{'name':name})