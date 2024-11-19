from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_type', 'profile_picture', 'phone_number', 'address')
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'user_type': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'user_type': 'نوع المستخدم',
            'profile_picture': 'الصورة الشخصية',
            'phone_number': 'رقم الهاتف',
            'address': 'العنوان',
        }

class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'profile_picture', 'phone_number', 'address')
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }