from rest_framework import serializers
from asesor.models import Asesor
from cliente.models import Cliente 
from producto.models import Producto
from factura.models import Factura, FacturaDetalle
from isla.models import Isla

class IslaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Isla
        fields = ('id',
                  'centroComercial',
                  'ciudad')
class AsesorSerializer(serializers.ModelSerializer):
    isla = IslaSerializer(many=False)
    class Meta:
        model = Asesor
        fields = ('id',
                  'nombre',
                  'apellido',
                  'correo',
                  'tipoDocumento',
                  'isla')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id',
                  'nombre',
                  'apellido',
                  'correo',
                  'tipoDocumento')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('codigo',
                  'nombre',
                  'valor',
                  'categoria')

class FacturaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(many=False)
    asesor = AsesorSerializer(many=False)
    class Meta:
        model = Factura
        fields = ('id',
                  'fecha',
                  'total',
                  'cliente',
                  'asesor')

class FacturaDetailSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(many=False)
    class Meta:
        model = FacturaDetalle
        fields = ('cantidad',
                  'valor',
                  'producto')



