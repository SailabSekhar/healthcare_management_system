from django.urls import path
from .views import pprofile,phome


urlpatterns = [


 path('phome',phome, name="phome"),
 path('pprofile',pprofile,name='pprofile')
]