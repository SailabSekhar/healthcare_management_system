from django.urls import path
from .views import dhome,dview,dprofile
urlpatterns = [
    path('dhome',dhome , name="dhome"),
    path('dview',dview, name="dview"),
    path('dprofile',dprofile, name="dprofile"),


]