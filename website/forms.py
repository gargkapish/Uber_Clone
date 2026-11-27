from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Full name', max_length=150)
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email']