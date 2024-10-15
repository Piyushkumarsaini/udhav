from rest_framework import serializers
from .models import *



class UserRegistrationSerializer(serializers.ModelSerializer):
        class Meta:
            model = UserRegistration # table name 
            fields = ['user_name', 'phone_and_email', 'password', 'date_of_brith', 'gender'] 
