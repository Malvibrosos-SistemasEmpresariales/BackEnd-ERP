from django.db import models
from cliente.models import Cliente

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    total = models.BigIntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    asesor = models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.nombre)