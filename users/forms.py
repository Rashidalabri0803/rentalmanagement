from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_customer', 'is_admin', 'password1', 'password2']
        labels = {
            'is_customer': 'تسجيل كعميل',
            'is_admin': 'تسجيل كمشرف',
        }

class CustomerLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={'placeholder': 'كلمة المرور'}),
        label='اسم المستخدم'
    )
    password = forms.CharField(
        widget= forms.PasswordInput(attrs={'placeholder': 'كلمة المرور'}),
        label='كلمة المرور'
    )
    