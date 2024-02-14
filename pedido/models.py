from django.db import models
from cuenta.models import Cuenta
from tienda.models import Producto
from django.utils import timezone


class Pago(models.Model):
    OPCION_METODO_PAGOS = [("Efectivo", "Efectivo"), ("Nequi", "Nequi")]

    OPCION_ESTADO_PAGOS = [
        ("Aceptado", "Aceptado"),
        ("Cancelado", "Cancelado"),
    ]

    usuario = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    pago_id = models.CharField(max_length=100)
    metodo_pago = models.CharField(max_length=50)
    # metodo_pago = models.CharField(max_length=50, choices=OPCION_METODO_PAGOS)
    cantidad_pagada = models.CharField(max_length=100)
    # numero_pago
    # El estado puede ser, Aceptado o cancelado
    # Que es en caso de que el admin valide si el comprobante es valido
    # Corregir que no sea blank=True
    comprobante = models.ImageField(upload_to="comprobantes/")
    estado_pago = models.CharField(max_length=50)

    # Tambien se puede crear como checkout
    # estado_pago = models.CharField(default=False)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.metodo_pago


class Pedido(models.Model):
    OPCION_DEPARTAMENTO = [
        # 1, se almacena en la base de datos, 2 se muestra en la interfaz
        ("Amazonas", "Amazonas"),
        ("Antioquía", "Antioquía"),
        ("Huila", "Huila"),
    ]

    OPCION_CIUDADES = [
        ("Leticia", "Leticia"),
        ("Medellin", "Medellin"),
        ("Neiva", "Neiva"),
    ]

    # null = acepta valores nulos
    # blank = Permite dejar el campo en blanco, opcional
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
    departamento = models.CharField(max_length=50, choices=OPCION_DEPARTAMENTO)
    ciudad = models.CharField(max_length=50, choices=OPCION_CIUDADES)
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
