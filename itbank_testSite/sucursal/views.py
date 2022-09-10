from .models import Sucursal
from .serializers import SucursalSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class SucursalList(APIView):
    def get(self, request):
        sucursales = Sucursal.objects.all()
        serializer = SucursalSerializer(sucursales, many=True)
        if sucursales:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'no sucursal found'}, status=status.HTTP_404_NOT_FOUND)
