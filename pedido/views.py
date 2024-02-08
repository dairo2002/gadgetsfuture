from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PedidoForm
from .models import Pedido
from carrito.models import Carrito, CarritoSesion

import datetime


# ! TERMINAR
# Validar si se esta enviando la informacion
# Continuar con el proceso de pago


@login_required(login_url="inicio_sesion")
def realizar_pedido(request, total=0, cantidad=0):
    usuario_actual = request.user
    carrito = Carrito.objects.filter(usuario=usuario_actual)
    contar_carrito = carrito.count()

    if contar_carrito <= 0:
        return redirect("tienda")

    for articulo in carrito:
        total += articulo.producto.precio * articulo.cantidad
        cantidad += articulo.cantidad
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            data = Pedido()
            data.usuario = usuario_actual
            data.nombre = form.cleaned_data["nombre"]
            data.apellido = form.cleaned_data["apellido"]
            data.telefono = form.cleaned_data["telefono"]
            data.correo_electronico = form.cleaned_data["correo_electronico"]
            data.direccion = form.cleaned_data["direccion"]
            data.direccion_local = form.cleaned_data["direccion_local"]
            data.departamento = form.cleaned_data["departamento"]
            data.ciudad = form.cleaned_data["ciudad"]
            data.total_pedido = total
            data.save

            # Numero del pedido: fecha del año, mes, y dia, pero tambien va ingrementado el pedido
            year = int(datetime.date.today().strftime("%Y"))
            months = int(datetime.date.today().strftime("%m"))
            day = int(datetime.date.today().strftime("%d"))

            dt = datetime.date(year, months, day)
            fecha_actual = dt.strftime("%Y%m%d")  # 2024 02 06
            numero_pedido = fecha_actual + (
                data.id
            )  # 2024 02 06 1.. ingremento por el id de cada pedido
            data.numero_pedido = numero_pedido
            data.save()

            # Ordenado es falso, cambia cuando realize el pago
            pedido = Pedido.objects.get(
                usuario=usuario_actual, ordenado=False, numero_pedido=numero_pedido
            )
            # Renderizamos pago porque necesitamos los datos tambien, ya que realizar pedido lo tremos lod datos del context_processors
            return render(
                request,
                "pedido/pago.html",
                {
                    "pedido": pedido,
                },
            )
    else:
        # redirect alguna parte,
        # return redirect('realizar_pedido')
        return redirect("")


def pago(request):
    return render(request, "pedido/pago.html")
