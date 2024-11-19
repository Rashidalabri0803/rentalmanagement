from django import forms

from .models import Booking, Review


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['property', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'property': 'العقار',
            'start_date': 'تاريخ البدء',
            'end_date': 'تاريخ الانتهاء',
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError('تاريخ البدء يجب أن يكون قبل تاريخ الانتهاء')
        return cleaned_data

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['property', 'rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'type': 'number', 'min': 1, 'max': 5, 'placeholder': 'من 1 إلى 5'}),
            'comment': forms.Textarea(attrs={'rows': 3, 'plceholder': 'اكتب تعليقك هنا...'}),
        }
        labels = {
            'property': 'العقار',
            'rating': 'التقييم (1-5)',
            'comment': 'التعليقات',
        }