from django import forms

from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'description', 'price_per_month', 'location', 'available']
        widgets = {
            'descriptiom': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'location': forms.TextInput(attrs={'placeholder': 'اكتب موقع العقار'}),
        }
        labels = {
            'name': 'اسم العقار',
            'description': 'وصف العقار',
            'price_per_month': 'السعر الشهري',
            'location': 'الموقع',
            'available': 'متاح للايجار',
        }