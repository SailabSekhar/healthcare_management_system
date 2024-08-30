from django.contrib import admin

# Register your models here.
from .models import signup_master

class signupadmin(admin.ModelAdmin):
    fields=['email','mobile','name','password','role_name']
    search_fields=["email","role_name"]
    list_filter=["mobile",'name']
    list_display=["email",'name',"mobile"]
    list_editable=["name",'mobile']
admin.site.register(signup_master,signupadmin)







