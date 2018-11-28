from django.db import models

class Producto(models.Model):
    códigoProducto = models.IntegerField()
    nombreProducto =  models.CharField(max_length=100)
    descripciónProducto = models.TextField()
    precioProducto = models.IntegerField()
    imagen =  models.FileField(max_length=None, upload_to='media')

    def __str__(self):
        return self.nombreProducto + '---' + self.descripciónProducto 
