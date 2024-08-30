from django.shortcuts import render
from .models import profile_master
from signup.models import signup_master

def viewprofile(request):
    email = request.session.get('email')
    
    if email:
        obj = signup_master.objects.get(email=email)  
        ob = profile_master.objects.filter(email=obj)
        return render(request, 'view.html', {'data': ob, 'data1': obj})
    else:
        return render(request, 'view.html', {'error': 'No email found in session'})

def profile_page(request):
    if request.method == "POST":
        email = request.session.get('email')
        fname = request.POST['fname']
        lname = request.POST['lname']
        image = request.FILES.get('image')
        document = request.FILES.get('doc')
        address = request.POST['address']
        
        obj = signup_master.objects.get(email=email)
        profile, created = profile_master.objects.get_or_create(
            email=obj,
            defaults={
                'fname': fname,
                'lname': lname,
                'image': image,
                'document': document,
                'address': address,
            }
        )
        if not created:
            profile.fname = fname
            profile.lname = lname
            if image:
                profile.image = image
            if document:
                profile.document = document
            profile.address = address
            profile.save()

        return render(request, 'profile.html', {'data': "Profile updated successfully..."})
    
    return render(request, 'profile.html')
