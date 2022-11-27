from django.db import models
from isla.models import Isla
from producto.models import Producto

class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    ini = models.IntegerField()
    ent = models.IntegerField()
    sal = models.IntegerField()
    fin = models.IntegerField()
    fecha = models.DateField()
    isla = models.ForeignKey(Isla, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)