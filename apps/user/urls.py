from django.urls import path 

from .views import CustomUserRegister


urlpatterns = [ 
    path('register/', CustomUserRegister.as_view(), name='user_register'),
]