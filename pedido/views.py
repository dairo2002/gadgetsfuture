from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PedidoForm
from .models import Pedido
from carrito.models import Carrito, CarritoSesion
from django.contrib import messages


import datetime


# ! TERMINAR
# Consultar si los datos se estan enviando (POST)
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
        return render(request, "pedido/realizar_pedido.html")
        # return render(request, "pedido/realizar_pedido.html", {"pedido": pedido})


def pago(request, id_pedido):
    pedido = get_object_or_404(Pedido, pk=id_pedido)
    return render(request, "pedido/pago.html", {"pedido": pedido})


def detalle_pedido(request):
    usuario_actual = request.user
    pedido = Pedido.objects.get(pk=usuario_actual)

    return render(request)
