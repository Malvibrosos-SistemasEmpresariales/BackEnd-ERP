from rest_framework import serializers 
from factura.models import Factura, FacturaDetalle

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ('id',
                  'fecha',
                  'total',
                  'cliente',
                  'asesor')

class FacturaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaDetalle
        fields = ('cantidad',
                  'valor',
                  'factura',
                  'producto')