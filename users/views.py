from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from  django.contrib import messages

from .forms import RegisterUserForm
from .models import User

# Create your views here.

def loginUser(request):
    if  request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "User does not exist!!!")
        user = authenticate(request,  email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Email Or Password does not exist!!!")
    context = {'page': 'login', 'form__title': 'LogIn'}
    return render(request, "users/register_login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    
    if  request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.avatar = request.FILES.get('avatar')
            user.username = request.POST.get('username').lower()
            user.save()
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = RegisterUserForm()
    
    context = {'form__title': 'SignUp', 'form': form}
    return render(request, "users/register_login.html", context)
    
