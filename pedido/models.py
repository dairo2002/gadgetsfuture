from django.db import models
from cuenta.models import Cuenta
from tienda.models import Producto


class Pago(models.Model):
    usuario = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    pago_id = models.CharField(max_length=100)
    metodo_pago = models.CharField(max_length=50)
    cantidad_pagada = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pago_id

class Pedido(models.Model):
    usuario = models.ForeignKey(Cuenta, on_delete=models.SET_NULL, null=True)
    pago = models.ForeignKey(Pago,  on_delete=models.SET_NULL, blank=True, null=True)
    numero_pedido = models.CharField(max_length=50)
    correo_electronico = models.CharField(max_length=100)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    direccion_local = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=50)    
    departamento = models.CharField(max_length=50)    
    ciudad = models.CharField(max_length=50)    
    ordenado = models.BooleanField(default=False)
    total_pedido = models.FloatField()

    # puede faltar el campo de estado del pedido

    def __str__(self):
        return self.nombre


class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    pago = models.ForeignKey(Pago, on_delete=models.SET_NULL, blank=True, null=True)
    usuario = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)                
    cantidad = models.IntegerField()
    precio = models.FloatField()
    ordenado = models.BooleanField(default=False)    
    

    def __str__(self):
        return self.producto.nombre
