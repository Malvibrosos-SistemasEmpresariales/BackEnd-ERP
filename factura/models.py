from django.db import models
from cliente.models import Cliente
from asesor.models import Asesor
from producto.models import Producto

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    total = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    asesor = models.ForeignKey(Asesor, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)

class FacturaDetalle(models.Model):
    cantidad = models.IntegerField()
    total = models.FloatField()
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)