from django.db import models

# Create your models here.

class UserRegistration(models.Model):
    user_name = models.CharField(max_length=100)
    phone_number = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_of_brith = models.DateField()
    gender = models.CharField(max_length=10, null=True, blank=True)
    # email = models.CharField(max_length=100,unique=True)
    # email = models.EmailField(unique=True)


    
    # def __str__(self):
    #     return self.user_name