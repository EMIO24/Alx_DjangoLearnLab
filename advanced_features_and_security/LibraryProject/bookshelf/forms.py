from django import forms
from .models import CustomUser  # Import your model

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # Link to your model
        fields = ['username', 'email', 'password']  # Specify fields to include
