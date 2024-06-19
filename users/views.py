from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import AppUserCreationForm


class SignUpView(CreateView):
    form_class = AppUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
