from django.db import models

# Create your models here.
class signup_master(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50,primary_key=True)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=30)
    role_name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
