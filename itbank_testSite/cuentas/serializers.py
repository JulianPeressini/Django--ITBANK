from rest_framework import serializers
from .models import Cuenta


class CuentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cuenta
        fields = '__all__'
        read_only_fields = (
            'account_id',
            'customer_id',
        )


class TipoCuentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cuenta
        fields = '__all__'
        read_only_fields = (
            'account_type_id',
            'account_type_desc',
        )
