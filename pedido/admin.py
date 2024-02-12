from django.contrib import admin
from .models import Pago, Pedido, PedidoProducto


class PagoAdmin(admin.ModelAdmin):
    list_display = (
        "usuario",
        "pago_id",
        "metodo_pago",
        "cantidad_pagada",
        "estado",
        "fecha",
    )


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
    cod_postal_upper.short_description = 'código_postal' 


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



#TODO revisar 
# class PedidoProductoInline(admin.TabularInline):
#     model = PedidoProducto
#     readonly_fields = ("pago_fk", "user_fk", "producto_fk", "cantidad", "producto_precio", 'ordenado')


admin.site.register(Pago, PagoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(PedidoProducto, PedidoProductoAdmin)
