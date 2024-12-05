from django import forms

from .models import BookingModel


class BookingForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ism:'}))
    from_location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Qayerdan:'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email:'}))
    to_location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Qayerga:'}))
    message = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'placeholder': 'Xabar:'}))

    class Meta:
        model = BookingModel
        fields = ['name', 'from_location', 'to_location', 'email', 'time', 'date', 'comfort', 'adults', 'children', 'message']
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }