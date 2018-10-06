from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """Provides form for User model"""

    email = forms.CharField(label='email')
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']


class RegisterForm(forms.ModelForm):
    """Provides form for User model"""
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='confirm_password',
                                       widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']