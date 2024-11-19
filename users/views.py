from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserCreationForm, CustomUserUpdateForm

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_verified = True
            user.save()
            return redirect('users:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('users:dashboard')
    return render(request, 'users/login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('users:login')

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:dashboard')
    else:
        form = CustomUserUpdateForm(instance=request.user)
    return render(request, 'users/update_profile.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.is_admin():
        return render(request, 'users/admin_dashboard.html')
    elif request.user.is_owner():
        return render(request, 'users/owner_dashboard.html')
    else:
        return render(request, 'users/customer_dashboard.html')