from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

# Create your views here.
def home_page(request):
    return render(request, 'register/home-page.html')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'username does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'home-page')
        else:
            messages.error(request,'username or password is incorrect')
            
    return render(request, 'register/login-register.html')


def logoutUser(request):
    logout(request)
    return redirect('home-page')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User Account Was Created!')
            login(request, user)
            return redirect('home-page')

        else:
            messages.error(request, 'An error has accurred during registration!')

    context = {'page' : page, 'form' : form}
    return render(request, 'register/login-register.html', context)
