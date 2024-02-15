from django.contrib import admin
from .models import Pago, Pedido, PedidoProducto
from django.utils.html import format_html


class PagoAdmin(admin.ModelAdmin):
    list_display = (
        "usuario",
        "pago_id",
        "metodo_pago",
        "cantidad_pagada",                
        "cargar_imagen",
        "estado_pago",
        "fecha",
    )

    # Funcion creada para cargar la imagen del comprobante en el admin
    def cargar_imagen(self, obj):
        if obj.comprobante:
            return format_html(
                '<img src="{}" width="100" height="100" alt="imagen comprobante">'.format(
                    obj.comprobante.url
                )
            )
        
    cargar_imagen.short_description = "Comprobante"



class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        "usuario",
        "pago",
        "numero_pedido",
        "correo_electronico",
        "nombre",
        "apellido",
        "telefono",
        "direccion",
        "direccion_local",
        # Se llama la funcion para la conversion a mayúsculas
        "cod_postal_upper",
        "departamento",
        "ciudad",
        "ordenado",
        "total_pedido",
    )

    def cod_postal_upper(self, obj):
        return obj.codigo_postal.upper()

    # Cambiar el nombre para ser mostradro en el admin
    cod_postal_upper.short_description = "código_postal"


class PedidoProductoAdmin(admin.ModelAdmin):
    list_display = (
        "pedido",
        "pago",
        "usuario",
        "producto",
        "cantidad",
        "precio",
        "ordenado",
    )


# TODO revisar
# class PedidoProductoInline(admin.TabularInline):
#     model = PedidoProducto
#     readonly_fields = ("pago_fk", "user_fk", "producto_fk", "cantidad", "producto_precio", 'ordenado')


admin.site.register(Pago, PagoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(PedidoProducto, PedidoProductoAdmin)
