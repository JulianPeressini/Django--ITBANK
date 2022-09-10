from django.shortcuts import render

from .models import Cliente
from empleados.models import Empleado
from .serializers import ClienteSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from clientes import serializers

# Create your views here.


def home(request):

    if request.user.is_authenticated:
        client = Cliente.objects.get(user=request.user.id)
        return render(request, "clientes/index.html", {'current_user': client})

    return render(request, "clientes/index.html")


class ClienteDetails(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        cliente = Cliente.objects.filter(customer_id=pk).first()
        serializer = ClienteSerializer(cliente)
        if cliente:
            if cliente.user_id == request.user.id:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'unauthorized': 'You can\'t access this data'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error': 'no cliente found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        cliente = Cliente.objects.filter(customer_id=pk).first()
        serializer = ClienteSerializer(cliente, data=request.data)
        if cliente:
            if serializer.is_valid():
                empleado = Empleado.objects.filter(
                    user_id=request.user.id).first()

                if empleado:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                elif cliente.user_id == request.user.id:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({'unauthorized': 'You can\'t access this data'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'error': 'invalid request'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'no cliente found'}, status=status.HTTP_404_NOT_FOUND)
