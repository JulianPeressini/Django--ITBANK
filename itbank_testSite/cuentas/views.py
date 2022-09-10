from .models import Cuenta, TipoCuenta
from clientes.models import Cliente
from .serializers import CuentaSerializer, TipoCuentaSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.


class CuentaDetails(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        cuentas = Cuenta.objects.filter(customer_id=pk)
        serializer = CuentaSerializer(cuentas, many=True)
        if len(cuentas) > 0:
            cliente = Cliente.objects.get(customer_id=cuentas[0].customer_id)
            if cliente.user_id == request.user.id:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'unauthorized': 'You can\'t access this data'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error': 'no results'}, status=status.HTTP_404_NOT_FOUND)
