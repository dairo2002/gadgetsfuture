from django.db import models
from tienda.models import Producto

class CarritoSesion(models.Model): 
    carrito_session = models.CharField(max_length=250, blank=True)
    fecha_agregado = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.carrito_session

class Carrito(models.Model):    
    carritoSesion = models.ForeignKey(CarritoSesion, on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    activo = models.BooleanField(default=True)
    fecha_agregado = models.DateField(auto_now_add=True)
    # igual a null, lo que indica que no están vinculados a ningún carrito específico. Esto podría ser útil si deseas mantener un historial de los artículos


    # Operacion para obtener un sub total del precio por la cantidad de un producto 
    def sub_total(self):
        return self.producto.precio * self.cantidad


    def __unicode__(self):
        return self.producto
