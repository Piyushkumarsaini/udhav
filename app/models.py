from django.db import models

# Create your models here.


class UserRegistration(models.Model):
    user_name = models.CharField(max_length=100)
    phone_and_email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=15,unique=True)
    date_of_brith = models.DateField()
    gender = models.CharField(max_length=10,blank=True,null=True)
    