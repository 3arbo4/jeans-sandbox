from django.shortcuts import render
# reverse_lazy routes based on login status
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login') # after successful SignUp, redirect to login page
                                        # reverse_lazy wont excute until user hit submit on the signup page
    template_name = 'accounts/signup.html'
