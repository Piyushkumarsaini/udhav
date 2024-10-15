from django.shortcuts import render
from .models import UserRegistration
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# @api_view(['GET'])
# def showdata(request):
#     obke = UserRegistration.objects.all()
#     print(obke)

#     # data = data
#     # print(data)
#     serializer = UserRegistrationSerializer(obke, many=True)
#     print(serializer)

#     return Response({'status': 200, 'message': 'User registered successfully!', 'data': serializer.data})

@api_view(['POST'])
def register(request):
    data = request.data
    
    serializer = UserRegistrationSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({'status': 200, 'message': 'User registered successfully!'})
    else:
        print(serializer.errors)  # Show any serializer errors in the console
        return Response({'status': 400, 'errors': serializer.errors})
    





















# {
#     "user_name": "testuser",
#     "phone_and_email": "testuser@example.com",
#     "password": "testpass123",
#     "date_of_brith": "2000-01-01",
#     "gender": "male"
# }