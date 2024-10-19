from django.shortcuts import render
from .models import UserRegistration
from .serializers import UserRegistrationSerializer, userloginserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def registration(request):
    data = request.data
    serializer = UserRegistrationSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({'status': 200, 'message': 'User registered successfully!'})
    else:
        return Response({'status': 400, 'errors': serializer.errors})
     


@api_view(['POST'])
def userlogin(request):
    data = request.data
    serializer = userloginserializer(data=data)
    if not serializer.is_valid():
        return Response({'status': 200, 'errors': serializer.errors})
    












































    
    # else:
    #     # return Response({'status': 400, 'errors': serializer.errors})
    #     return Response({'status': 200, 'message': 'User login successfully!'})


    

# @api_view(['POST'])
# def userlogin(request):
#     data = request.data
    
#     serializer = UserRegistrationSerializer(data=data)
   

#     if serializer.is_valid():
#         serializer.save()
#         return Response({'status': 200, 'message': 'User registered successfully!'})
#     else:
#         print(serializer.errors)  # Show any serializer errors in the console
#         return Response({'status': 400, 'errors': serializer.errors})    
# @api_view(['PUT'])
# def update_registration(request, id):
#     try:
#         registration_object = UserRegistration.objects.get(id = id)
#         print(registration_object)
#         # serializer = UserRegistrationSerializer(registration_object, many=True)

#         serializer = UserRegistrationSerializer(registration_object, data=request.data)
    
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status': 200, 'message': 'User registered successfully!'})
#         else:
#             print(serializer.errors)  # Show any serializer errors in the console
#             return Response({'status': 400, 'errors': serializer.errors})

#     except Exception as e:
#         return Response({'status': 403, 'message': 'invali'}) 












# {
#     "user_name": "testuser",
    # "phone_number": 657464756,
    # "email": "testuser@example.com",
    # "password": "testpass123",
#     "date_of_brith": "2000-01-01",
#     "gender": "male"
# }