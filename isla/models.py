from django.db import models

class Isla(models.Model):
    id = models.AutoField(primary_key=True)
    centroComercial = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.nombre)
