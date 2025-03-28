from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.forms import forms
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ExtendedUserCreationForm, UserForm, ProfileForm
from .models import Profile


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            for error in form.errors.values():
                messages.error(request, error.as_text())
    else:
        form = ExtendedUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile(request):
    try:
        profile_obj = request.user.profile
    except Profile.DoesNotExist:
        profile_obj = Profile(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile_obj)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'There was an error updating your profile.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile_obj)

    return render(request, 'blog/profile.html', {'user_form': user_form, 'profile_form': profile_form})
