from django import forms
from .models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            "nombre",
            "apellido",
            "correo_electronico",
            "telefono",
            "direccion",
            "direccion_local",
            "departamento",
            "ciudad",
            "codigo_postal",
        ]