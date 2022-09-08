from multiprocessing.sharedctypes import Value
from socket import fromshare
from unicodedata import name
from django import forms
from django.forms import TextInput


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'login-input', 'placeholder': 'Escriba su usuario...', 'name': 'username'}), label='')
    password = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'login-input', 'placeholder': 'Escriba su contraseña...', 'type': 'password', 'name': 'password'}), label='')
