from distutils.log import info
from http import client
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Prestamo
from .forms import PrestamoForm
from clientes.models import Cliente
from cuentas.models import Cuenta
from django.contrib import messages


# Create your views here.


def Prestamos(request):

    if request.user.is_authenticated:

        client = Cliente.objects.get(user=request.user.id)
        cuentas = Cuenta.objects.filter(customer_id=client.customer_id)
        account_choices = []

        for i in range(len(cuentas)):
            account_choices.append((cuentas[i].iban, cuentas[i].iban))

        if request.method == "POST":
            prestamo_form = PrestamoForm(request.POST, user=request.user)
            prestamo_form.fields['cuenta'].choices = account_choices

            if prestamo_form.is_valid():
                tipo = request.POST.get('tipo')
                fecha = request.POST.get('date')
                monto = request.POST.get('monto')
                cuenta = request.POST.get('cuenta')
                prestamo_final = Prestamo(
                    loan_type=tipo, loan_date=fecha, loan_total=monto, customer_id=client.customer_id)
                cuenta_update = Cuenta.objects.get(iban=cuenta)
                cuenta_update.balance += int(monto)
                prestamo_final.save()
                cuenta_update.save()
                return redirect('/')
        else:
            prestamo_form = PrestamoForm(user=request.user)
            prestamo_form.fields['cuenta'].choices = account_choices

        return render(request, "prestamos/prestamos.html", {'form': prestamo_form})
    else:
        return redirect('/login')
