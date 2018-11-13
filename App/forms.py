from django import forms
from django.contrib.auth.models import User
from App.models import Project

class ProjectForm(forms.ModelForm):
    """Provides form for Project model"""

    class Meta:
        model = Project
        fields = ['semester', 'course_name', 'project_name', 'project_description', 'member', 'faculty','student_mentor', 'file_upload']


class LoginForm(forms.Form):
    """Provides form for User model"""

    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
    """Provides form for User model"""
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password',
                                       widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','username', 'password', 'confirm_password']