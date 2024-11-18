from django.contrib.auth import login, logout, aauthenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .models import User
from .forms import CustomerLoginForm, CustomerUserCreationForm, CustomUserUpdateForm


def register_user(request):
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = CustomerUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = CustomerLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users:dashboard')
    else:
        form = CustomerLoginForm()
    return render(request, 'users/login.html', {'form': form})

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
    if request.user.is_admin:
        return render(request, 'users/admin_dashboard.html')
    else:
        return render(request, 'users/customer_dashboard_customer.html')

def unauthorized(request):
    return render(request, 'users/unauthorized.html', status=403)