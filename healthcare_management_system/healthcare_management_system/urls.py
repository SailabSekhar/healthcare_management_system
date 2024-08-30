"""
URL configuration for healthcare_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views as hviews
from add.views import add 
from signup.views import signup
from login.views import login,logout_view
from change_profile.views import profile_page,viewprofile
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path,include
urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('myadmin/', include('myadmin.urls')),
    
    #change_profile
    path('profile_page',profile_page,name='profile_page'),
    path('viewprofile',viewprofile,name='viewprofile'),

    #doctor
    
    path('doctor/', include('doctor.urls')),

    #patient
    path('patient/', include('patient.urls')),
   
   
    

    path('admin/', admin.site.urls),
    #login
    path('login',login , name="login"),
    #signup
    path('signup',signup ,name="signup"),

    #add
    path('add', add ),
    #home
    path('',hviews.index,name="dashboard"),
    path('home',hviews.home,name="home"),
    path("about",hviews.about),
    path('contact',hviews.contact),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



