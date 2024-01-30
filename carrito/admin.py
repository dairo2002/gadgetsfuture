from django.contrib import admin
from .models import Carrito, CarritoSesion


class CarritoSesionAdmin(admin.ModelAdmin):
    list_display = (
        "carrito_session",
        "fecha_agregado",
    )


class CarritoAdmin(admin.ModelAdmin):
    list_display = (
        "carritoSesion",
        "producto",
        "cantidad",
        "activo",
    )

admin.site.register(CarritoSesion, CarritoSesionAdmin)
admin.site.register(Carrito, CarritoAdmin)
