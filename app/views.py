from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        phone_or_email = request.POST['phone_and_email']
        return HttpResponse("User registered successfully!")