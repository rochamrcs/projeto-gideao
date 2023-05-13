from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, './home.html')


def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user =  authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, './home.html' )
    else:
        return render(request, './login.html' )