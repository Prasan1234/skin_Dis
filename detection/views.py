from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserLoginForm, ImageUploadForm, UserRegistrationForm
from .models import UploadedImage, UserProfile
from django.contrib.auth.models import User

def home_page(request):
    return render(request, 'detection/home.html')

def user_login(request):
    error_message = None
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_page')
            else:
                error_message = "Invalid username or password. Please try again."
    else:
        form = UserLoginForm()
    return render(request, 'detection/login.html', {'form': form, 'error_message': error_message})

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save(commit=False)
            image_instance.user = request.user
            image_instance.save()
            return redirect('user_page')
    else:
        form = ImageUploadForm()
    return render(request, 'detection/upload_image.html', {'form': form})

def user_page(request):
    user_images = UploadedImage.objects.filter(user=request.user)
    return render(request, 'detection/user_page.html', {'user_images': user_images})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the login page after successful registration
            return redirect('login')  # Update this line
    else:
        form = UserCreationForm()
    return render(request, 'detection/register.html', {'form': form})


def verify_otp(request, user_id):
    user_profile = UserProfile.objects.get(user_id=user_id)
    if request.method == 'POST':
        otp_entered = request.POST.get('otp')
        if otp_entered == str(user_profile.otp):
            user = user_profile.user
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('user_page')
        else:
            return render(request, 'detection/verify_otp.html', {'error': 'Invalid OTP'})
    return render(request, 'detection/verify_otp.html')
