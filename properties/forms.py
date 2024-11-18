from django import forms

from .models import Property, PropertyImage, PropertyCatagory


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'description', 'price_per_month', 'location', 'category', 'available']
        widgets = {
            'descriptiom': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'location': forms.TextInput(attrs={'placeholder': 'اكتب موقع العقار'}),
        }
        labels = {
            'name': 'اسم العقار',
            'description': 'وصف العقار',
            'price_per_month': 'السعر الشهري',
            'location': 'الموقع',
            'category': 'فئة العقار',
            'available': 'متاح للايجار',
        }

class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ['image', 'caption']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'caption': forms.TextInput(attrs={'placeholder': 'وصف الصورة'}),
        }
        labels = {
            'image': 'الصورة',
            'caption': 'وصف الصورة',
        }

class PropertyCatagoryForm(forms.ModelForm):
    class Meta:
        model = PropertyCatagory
        fields = ['name', 'description']
        labels = {
            'name': 'اسم الفئة',
            'description': 'وصف الفئة',
        }