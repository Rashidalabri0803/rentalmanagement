from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User

class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_customer', 'is_admin', 'password1', 'password2']
        labels = {
            'is_customer': 'تسجيل كعميل',
            'is_admin': 'تسجيل كمشرف',
        }
        widgets = {
            'profile_picture': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_picture']
        widgets = {
            'profile_picture': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class CustomerLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={'placeholder': 'كلمة المرور'}),
        label='اسم المستخدم',
    )
    password = forms.CharField(
        widget= forms.PasswordInput(attrs={'placeholder': 'كلمة المرور'}),
        label='كلمة المرور',
    )
    