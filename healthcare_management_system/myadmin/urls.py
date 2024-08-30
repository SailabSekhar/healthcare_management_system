from django.contrib import admin
from django.urls import path
from .views import aviewdata,ahome,update
urlpatterns = [
path('aviewdata',aviewdata, name="aviewdata"),
path('ahome',ahome, name="ahome"),
path('update',update,name='update'),
]