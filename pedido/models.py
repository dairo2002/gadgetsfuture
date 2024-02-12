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
    departamentos_opciones = [
        # 1, se almacena en la base de datos, 2 se muestra en la interfaz
        ("Amazonas", "Amazonas"),
        ("Antioquía", "Antioquía"),
        ("Huila", "Huila"),
    ]

    ciudades_opciones = [
        ("Leticia", "Leticia"),
        ("Medellin", "Medellin"),
        ("Neiva", "Neiva"),
    ]


    # null = acepta valores nulos
    # blank = Permite dejar el campo el blanco, opcional
    usuario = models.ForeignKey(Cuenta, on_delete=models.SET_NULL, null=True)
    pago = models.ForeignKey(Pago, on_delete=models.SET_NULL, blank=True, null=True)
    numero_pedido = models.CharField(max_length=50)
    correo_electronico = models.EmailField(max_length=100)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ordenado = models.BooleanField(default=False)
    direccion_local = models.CharField(max_length=50, blank=True)
    departamento = models.CharField(max_length=50, choices=departamentos_opciones)
    ciudad = models.CharField(max_length=50, choices=ciudades_opciones)
    codigo_postal = models.CharField(max_length=50)
    total_pedido = models.FloatField()

    # puede faltar el campo de estado del pedido
    def __str__(self):
        return self.nombre

    def nombre_completo_pedido(self):
        return f"{self.nombre} {self.apellido}"

    def direccion_completa(self):
        return f"{self.direccion} {self.direccion_local}"


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
