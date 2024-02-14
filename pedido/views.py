from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PedidoForm, PagoForm
from .models import Pedido, Pago
from carrito.models import Carrito, CarritoSesion
from django.contrib import messages


import datetime


# ! TERMINAR
# Continuar con el proceso de pago


@login_required(login_url="inicio_sesion")
def realizar_pedido(request, total=0, cantidad=0):
    usuario_actual = request.user
    carrito = Carrito.objects.filter(usuario=usuario_actual)
    contar_carrito = carrito.count()
    pedido = 0

    if contar_carrito <= 0:
        return redirect("tienda")

    for articulo in carrito:
        total += articulo.producto.precio * articulo.cantidad
        cantidad += articulo.cantidad
    if request.method == "POST":
        formulario = PedidoForm(request.POST)
        if formulario.is_valid():
            data = Pedido()
            data.usuario = usuario_actual
            data.nombre = formulario.cleaned_data["nombre"]
            data.apellido = formulario.cleaned_data["apellido"]
            data.telefono = formulario.cleaned_data["telefono"]
            data.correo_electronico = formulario.cleaned_data["correo_electronico"]
            data.direccion = formulario.cleaned_data["direccion"]
            data.direccion_local = formulario.cleaned_data["direccion_local"]
            data.departamento = formulario.cleaned_data["departamento"]
            data.ciudad = formulario.cleaned_data["ciudad"]
            data.codigo_postal = formulario.cleaned_data["codigo_postal"]
            data.total_pedido = total
            data.save()  # Guarda el pedido, para hacer uso del ID en el numero de pedido

            # Numero del pedido: fecha del año, mes, y dia, pero tambien va ingrementado el pedido
            year = int(datetime.date.today().strftime("%Y"))
            months = int(datetime.date.today().strftime("%m"))
            day = int(datetime.date.today().strftime("%d"))

            dt = datetime.date(year, months, day)
            fecha_actual = dt.strftime("%Y%m%d")  # 2024 02 06
            # 2024 02 06 1.. ingremento por el id de cada pedido
            num_pedido = fecha_actual + str(data.id)
            data.numero_pedido = num_pedido
            data.save()

            # Ordenado es falso, cambia cuando realize el pago
            # pedido = Pedido.objects.get(
            #     usuario=usuario_actual, ordenado=False, numero_pedido=numero_pedido
            # )
            return redirect("pago", id_pedido=data.pk)
    else:
        formulario = PedidoForm()
        return render(request, "pedido/realizar_pedido.html", {"form": formulario})
        # return render(request, "pedido/realizar_pedido.html", {"pedido": pedido})


def pago(request, id_pedido):
    pedido = get_object_or_404(Pedido, pk=id_pedido)
    if request.method == "POST":
        formulario = PagoForm(request.POST, request.FILES)
        if formulario.is_valid():
            print("Datos del formulario:", formulario.cleaned_data)
            data = Pago()
            data.metodo_pago = formulario.cleaned_data["metodo_pago"]
            data.comprobante = formulario.cleaned_data["comprobante"]
            data.usuario = request.user
            data.pago_id = pedido.pk
            data.estado_pago = pedido.pk
            data.cantidad_pagada = pedido.total_pedido
            print("Datos antes de guardar:", data.__dict__)
            data.save()

            print("Datos después de guardar:", data.__dict__)
            pedido.ordenado = True
            pedido.save()
            # Mensaje de borrador para saber si los datos fueron enviados
            messages.success(
                request, "Realizado el pago, Se retificara el comprobante si es valido"
            )
            return redirect("index")
        else:
            messages.error(request, "Por favor corrija los errores en el formulario.")
    else:
        formulario = PagoForm()
    return render(request, "pedido/pago.html", {"pedido": pedido, "form": formulario})


def detalle_pedido(request):
    usuario_actual = request.user
    pedido = Pedido.objects.get(pk=usuario_actual)

    return render(request)
