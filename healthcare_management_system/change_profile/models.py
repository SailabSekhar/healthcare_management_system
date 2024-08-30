from django.db import models
from signup.models import signup_master

# Create your models here.
class profile_master(models.Model):
    email=models.ForeignKey(signup_master,on_delete=models.CASCADE,default=None)
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    image=models.ImageField(upload_to="images/")
    document=models.FileField(upload_to="documents/")
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.fname
    class Meta:
        unique_together = ('email',)