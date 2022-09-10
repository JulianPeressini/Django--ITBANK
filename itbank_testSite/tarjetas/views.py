from .models import Tarjeta
from clientes.models import Cliente
from empleados.models import Empleado
from .serializers import TarjetaSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class ClientTarjetaList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        cliente = Cliente.objects.filter(customer_id=pk).first()
        if cliente:
            tarjetas = Tarjeta.objects.filter(customer_id=cliente.customer_id)
            serializer = TarjetaSerializer(tarjetas, many=True)
            empleado = Empleado.objects.filter(user_id=request.user.id)
            if empleado:

                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'unauthorized': 'You can\'t access this data'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error': 'no cliente found'}, status=status.HTTP_404_NOT_FOUND)
