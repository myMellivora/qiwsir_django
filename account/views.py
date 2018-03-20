from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
