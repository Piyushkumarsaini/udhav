from rest_framework import serializers
import re
from .models import *
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

# import checke_password

User = get_user_model()



class UserRegistrationSerializer(serializers.ModelSerializer):
      class Meta:
            model = UserRegistration # table name 
            fields = ['user_name', 'phone_number', 'email', 'pasword', 'date_of_brith', 'gender']
        

      def validate_phone_number(self, value):
            if len(str(value)) != 10:
                  raise serializers.ValidationError("Please enter a valid phone number.")
            return value
      

      def validate_password(self, value):
            if len(value) < 8:
                  raise serializers.ValidationError("Password must be at least 8 characters long.")
            return value
      
        
        # def validate_email(self, data):
        #     email = str(data)
        #     email_regex = r'^[a-zZ-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2.}$'
        #     if not re.match(email_regex,email):
        #         raise serializers.ValidationError({'error': 'please enter a valid email'})
        #     return data
        


class userloginserializer(serializers.ModelSerializer):
      class Meta:
            model = UserRegistration
            fields = ['email', 'password']

      def validate(self, data):
            email = data.get('email', None)
            password = data.get('password', None)

            try:
                  user = UserRegistration.objects.get(email=email, password=password)
            except:
                  raise serializers.ValidationError({'message': 'user does not exist'})
            

            # try:
            #       get_password = UserRegistration.objects.filter(password=password)
            # except UserRegistration.DoesNotExist:
            #       raise serializers.ValidationError({'message': 'Incorrect password'})
                        
            return data






















      # def create(self, validated_data):
      #       validated_data['password'] = make_password(validated_data['password'])
      #       user = User.objects.create(**validated_data)
      #       return user
    
      
       


    # def create(self, validated_data):
      #       validated_data['password'] = make_password(validated_data['password'])
      #       user = User.objects.create(**validated_data)
      #       return user


      #   def create(self, validated_data):
      #       user = User.objects.create(
      #             user_name=validated_data['user_name'],
      #             phone_number=validated_data['phone_number'],
      #             email=validated_data['email'],
      #             password=validated_data['password'],  # You can hash the password here
      #             date_of_brith=validated_data['date_of_brith'],
      #             gender=validated_data['gender']
      #       )
      #       return user

            # if not UserRegistration.objects.filter(email=email):
            #       raise serializers.ValidationError({'message': 'email does not exist'})
            # user = UserRegistration.objects.get(email=email)
 
            # if not user.check_password(password):
            #       raise serializers.ValidationError({'message': 'incorret password'})
            
            # return data




      # # def validate_email(self, data):
      # #       email = str(data)
      # #       if not UserRegistration.objects.filter(email=email):
      # #             raise serializers.ValidationError({'message': 'email does not exist'}) 
      # #       return data
      



      # def validate_password(self, data):
      #       password = str(data)
      #       get_password = UserRegistration.objects.filter(password=password)
      #       if get_password == password:
      #            raise serializers.ValidationError({'error': 'incorrect password'})
      #       return data
      
      
      # def validate_password(self, data):
      #       password = str(data)
      #       if UserRegistration.objects.filter(password=password):
      #             return serializers.ValidationError({'message': 'User login successfully!'})          
      #       return data


      # def validate_phone_number(self, data):
      #       phone_number = data.get('phone_number')
      #       if len(str(phone_number)) != 10:
      #             raise serializers.ValidationError({'error': 'please enter a valid number'})
            
      #       if not phone_number:
      #             raise serializers.ValidationError({'error': 'phone number is required'})
            
      #       try:
      #             user = UserRegistration.objects.get(phone_number=phone_number)
      #       except UserRegistration.DoesNotExist:
      #             raise serializers.ValidationError({'error': 'phone number does not exist'})  
                    
      #       return data
      

      
 




