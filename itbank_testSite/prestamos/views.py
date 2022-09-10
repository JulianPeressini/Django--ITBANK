from asyncio.windows_events import NULL
from hashlib import new
from django.shortcuts import render
from django.shortcuts import redirect

import prestamos

from .models import Prestamo
from clientes.models import Cliente
from cuentas.models import Cuenta
from sucursal.models import Sucursal
from empleados.models import Empleado
from .forms import PrestamoForm
from .serializers import PrestamoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


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


class PrestamoList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = PrestamoSerializer(data=request.data)
        if serializer.is_valid():
            empleado = Empleado.objects.filter(user_id=request.user.id)

            if empleado:
                cuenta_update = Cuenta.objects.filter(
                    customer_id=serializer.validated_data['customer_id']).first()
                cuenta_update.balance += serializer.validated_data['loan_total']
                cuenta_update.save()
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'unauthorized': 'You can\'t perform this action'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error': 'invalid request'}, status=status.HTTP_400_BAD_REQUEST)


class PrestamoDetails(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        prestamos = Prestamo.objects.filter(customer_id=pk)
        serializer = PrestamoSerializer(prestamos, many=True)
        if len(prestamos) > 0:
            cliente = Cliente.objects.get(customer_id=prestamos[0].customer_id)
            if cliente.user_id == request.user.id:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'unauthorized': 'You can\'t access this data'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error': 'no prestamo found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        prestamo = Prestamo.objects.filter(loan_id=pk).first()

        if prestamo:
            serializer = PrestamoSerializer(prestamo)
            empleado = Empleado.objects.filter(user_id=request.user.id)

            if empleado:

                cuenta_update = Cuenta.objects.filter(
                    customer_id=prestamo.customer_id).first()
                cuenta_update.balance -= prestamo.loan_total
                cuenta_update.save()
                prestamo.delete()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'unauthorized': 'You can\'t perform this action'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error': 'invalid request'}, status=status.HTTP_400_BAD_REQUEST)


class SucursalPrestamoList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        sucursal = Sucursal.objects.filter(branch_id=pk).first()
        if sucursal:
            clientes = Cliente.objects.filter(branch_id=sucursal.branch_id)
            if len(clientes) > 0:
                prestamos = Prestamo.objects.filter(customer_id__in=clientes)
                if len(prestamos) > 0:
                    serializer = PrestamoSerializer(prestamos, many=True)
                    empleado = Empleado.objects.filter(
                        user_id=request.user.id)
                    if empleado:
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    else:
                        return Response({'unauthorized': 'You can\'t access this data'}, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response({'error': 'no prestamos found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error': 'no clientes found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'no sucursal found'}, status=status.HTTP_404_NOT_FOUND)
