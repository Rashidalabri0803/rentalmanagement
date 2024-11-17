from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CustomerLoginForm, CustomerUserCreationForm


def register_user(request):
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomerUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = CustomerLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomerLoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    if request.user.is_admin:
        return render(request, 'users/admin_dashboard.html')
    else:
        return render(request, 'users/customer_dashboard_customer.html')

def unauthorized(request):
    return render(request, 'users/unauthorized.html', status=403)