from cProfile import label
from datetime import datetime
from distutils import errors
from multiprocessing.sharedctypes import Value
from socket import fromshare
from tkinter import Widget
from unicodedata import name
from xml.dom import ValidationErr
from xml.sax.xmlreader import InputSource
from django import forms
from django.forms import TextInput
from django.forms import Select
from django.forms import NumberInput
from django.forms import DateInput
from clientes.models import Cliente


def check_client_type(monto, user):
    client = Cliente.objects.get(user=user.id)

    if monto > 500000:
        return False
    elif monto > 300000:
        if client.client_type == 3:
            return True
        else:
            return False
    elif monto > 100000:
        if client.client_type == 2:
            return True
        else:
            return False
    else:
        return True


class PrestamoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PrestamoForm, self).__init__(*args, **kwargs)

    TYPECHOICES = [('Hipotecario', 'Hipotecario'),
                   ('Personal', 'Personal'), ('Prendario', 'Prendario')]

    tipo = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'prestamo-input', 'name': 'tipo'}), choices=TYPECHOICES, label='Tipo')

    cuenta = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'prestamo-input', 'name': 'cuenta'}), label='Cuenta')

    def clean_cuenta(self):
        data = self.cleaned_data.get('cuenta')

        return data

    monto = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'prestamo-input', 'name': 'monto', 'placeholder': '0'}), label='Monto')

    def clean_monto(self):
        data = self.cleaned_data.get('monto')
        if not check_client_type(data, self.user):
            raise forms.ValidationError(
                'El monto excede el limite para este tipo de cliente')

        if data <= 0:
            raise forms.ValidationError('Ingrese un monto de valor positivo')

        return data

    date = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'prestamo-input', 'placeholder': 'yyyy-mm-dd', 'name': 'date'}), label="Fecha de inicio", input_formats=['%Y-%m-%d'], error_messages=({'invalid': 'Ingrese un formato de fecha valido (yyyy-mm-dd)'}))
