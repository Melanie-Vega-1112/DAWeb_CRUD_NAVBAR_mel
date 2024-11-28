from django.db import models

# Create your models here.

class  Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True,)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    categoria = models.CharField(max_length=45)
    material = models.CharField(max_length=50)
    stock = models.IntegerField()
    id_proveedores = models.IntegerField()

    def __str__(self):
        return self.nombre
    