from django.db import models

class Cliente(models.Model):
    TIPOS = (("CC", "CC"), ("TI", "TI"), ("CE", "CE"), ("Passport", "Passport"))
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    tipoDocumento = models.CharField(max_length=8, choices = TIPOS)
    def __str__(self):
        return '{}'.format(self.nombre)