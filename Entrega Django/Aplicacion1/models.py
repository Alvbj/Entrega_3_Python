from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    razon_social = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre} {self.razon_social}'

class Proveedores(models.Model):
    proveedor = models.CharField(max_length=30)
    tipo = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.proveedor} {self.tipo}'

class Productos(models.Model):
    producto = models.CharField(max_length=30)
    subrubro = models.CharField(max_length=10)
    rubro = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.producto} {self.subrubro} {self.rubro}'