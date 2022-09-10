from rest_framework import serializers
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = (
            'customer_id',
            'user',
            'customer_name',
            'customer_surname',
            'customer_dni',
            'dob',
            'branch_id',
            'client_type'
        )
