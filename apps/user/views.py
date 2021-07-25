from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView 

from .models import CustomUser
from .forms import CustomUserCreationForm


class CustomUserRegister(CreateView):
    model = CustomUser 
    form_class = CustomUserCreationForm
    template_name = 'user/profile/register.html'
    success_url = reverse_lazy('home')