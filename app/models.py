from nturl2path import url2pathname
from pydoc import describe
from django.db import models

# Create your models here.

class user_registration(models.Model):
    fullname = models.CharField(max_length=240, null=True)
    username = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    joiningdate = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    
class user_scrapdatahistory(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,null=True,blank=True)
    History = models.CharField(max_length=240, null=True)
    date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)

class admin_data(models.Model):
    Heading = models.CharField(max_length=240, null=True)
    Describe = models.CharField(max_length=2404, null=True)
    url = models.CharField(max_length=240, null=True)
    filez = models.FileField(upload_to='images/', null=True, blank=True)

