from django.db import models

# Create your models here.

class user_registration(models.Model):
    fullname = models.CharField(max_length=240, null=True)
    username = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    
    