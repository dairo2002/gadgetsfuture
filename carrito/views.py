from django.shortcuts import render, redirect, get_object_or_404
from tienda.models import Producto
from .models import CarritoSesion, Carrito
from django.urls import resolve

# from carrito.context_processors import _carrito_sesion


def _carrito_sesion(request):
    # Obtener la clave de sesión actual del usuario
    carrito = request.session.session_key
    # Verificar si el usuario tiene una sesión activa (si carrito es nulo o vacío)
    if not carrito:
        # Si no hay una sesión activa, crear una nueva sesión y obtener su clave
        carrito = request.session.create()
        # Devolver la clave de sesión (puede ser la existente o la recién creada)
    return carrito


def add_carrito(request, producto_id):
    productos = get_object_or_404(Producto, pk=producto_id)
    try:
        carrito_sesion = CarritoSesion.objects.get(
            carrito_session=_carrito_sesion(request)
        )
    except CarritoSesion.DoesNotExist:
        carrito_sesion = CarritoSesion.objects.create(
            carrito_session=_carrito_sesion(request)
        )
    carrito_sesion.save()

    try:
        carrito = Carrito.objects.get(carritoSesion=carrito_sesion, producto=productos)
        carrito.cantidad += 1
        carrito.save()
    except Carrito.DoesNotExist:
        carrito = Carrito.objects.create(
            producto=productos, cantidad=1, carritoSesion=carrito_sesion
        )
        carrito.save()

    return redirect("mostrar_carrito")


# Vista que va hacia el carrito
def mostrar_carrito(request):
    return render(request, "tienda/carrito.html")


# Eliminar un producto por la cantidad
def delete_cantidad_carrito(request, producto_id):
    carrito_sesion = CarritoSesion.objects.get(carrito_session=_carrito_sesion(request))
    producto = get_object_or_404(Producto, pk=producto_id)

    carrito = Carrito.objects.get(producto=producto, carritoSesion=carrito_sesion)
    #  Actualización de la cantidad del carrito
    if carrito.cantidad > 1:
        # Si la cantidad es mayor que 1, se disminuye en 1 y se guarda
        carrito.cantidad -= 1
        carrito.save()
    else:
        # Eliminación del producto del carrito si la cantidad es 1 o menos
        carrito.delete()
    return redirect("mostrar_carrito")


def delete_producto_carrito(request, producto_id):
    carrito_sesion = CarritoSesion.objects.get(carrito_session=_carrito_sesion(request))
    producto = get_object_or_404(Producto, pk=producto_id)

    carrito = Carrito.objects.get(producto=producto, carritoSesion=carrito_sesion)
    carrito.delete()
    return redirect("mostrar_carrito")
