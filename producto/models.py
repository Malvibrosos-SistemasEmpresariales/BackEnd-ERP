from django.db import models

# Create your models here.
class Producto(models.Model):
    CATEGORIAS = (("HairTools", "HairTools"), ("Accessories", "Accessories"), ("HairCare", "HairCare"), ("SAMacho", "SAMacho"))
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    valor = models.IntegerField()
    categoria = models.CharField(max_length=12, choices = CATEGORIAS)
    def __str__(self):
        return '{}'.format(self.nombre)