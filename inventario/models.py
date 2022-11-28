from django.db import models
from isla.models import Isla
from producto.models import Producto

class Inventario(models.Model):
    cantidad = models.IntegerField()
    isla = models.ForeignKey(Isla, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, primary_key= True)
    def __str__(self):
        return '{}'.format(self.nombre)

class InventarioMovimientos(models.Model):
    cantidad = models.IntegerField()
    fecha = models.DateField()
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)