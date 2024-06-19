from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import AppUser


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = AppUser
        fields = ('username', 'first_name', 'last_name', 'email', 'date_birth')


class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = AppUser
        fields = ('username', 'first_name', 'last_name', 'email', 'date_birth')
