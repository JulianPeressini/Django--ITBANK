from rest_framework import serializers
from .models import Tarjeta


class TarjetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarjeta
        fields = '__all__'
        read_only_fields = (
            'card_id',
            'card_number',
            'card_security_code',
            'card_issue_date',
            'card_type',
            'customer_id',
        )



