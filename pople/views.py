from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')  # Home sahifasiga yo'naltirish
        else:
            messages.error(request, 'Login yoki parol noto‘g‘ri!')
    return render(request, 'login.html')
  

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Foydalanuvchini saqlash
            login(request, user)  # Yangi foydalanuvchini tizimga kiriting
            return redirect('user_profile_page')  # Ro'yxatdan o'tgan foydalanuvchini profil sahifasiga yo'naltirish
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})