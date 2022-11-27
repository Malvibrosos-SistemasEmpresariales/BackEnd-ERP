from django.db import models
from isla.models import Isla

class Asesor(models.Model):
    TIPOS = (("CC", "CC"), ("CE", "CE"), ("Passport", "Passport"))
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    tipoDocumento = models.CharField(max_length=8, choices = TIPOS)
    isla = models.ForeignKey(Isla, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)