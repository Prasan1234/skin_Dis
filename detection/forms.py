from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UploadedImage
import random

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    otp = forms.IntegerField(widget=forms.HiddenInput(), required=False)  # Add OTP field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

   

