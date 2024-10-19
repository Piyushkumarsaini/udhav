from django.urls import path,include
from . import views

urlpatterns = [
    path('api/registration/', views.registration, name='registration'),
    path('api/login', views.userlogin, name='login'),
    # path('update/<id>/',views.update_registration, name='update_registration'),

]
