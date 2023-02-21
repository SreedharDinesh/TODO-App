from django import forms
from .models import Register, Login


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'password']