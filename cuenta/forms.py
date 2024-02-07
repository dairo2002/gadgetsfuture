import re
from typing import Any
from django import forms
from .models import Cuenta

# Validacion email
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Crear el formulario de Registro


class RegistroForms(forms.ModelForm):
    # Se crean estos campos que no estan en el modelo
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"placeholder": "Ingresar contraseña"}),
    )

    confirm_pwd = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirmar contraseña"}),
    )

    class Meta:
        model = Cuenta
        # Traemos los campos del modelo de cuenta, que son aplicados al formulario,
        fields = ["nombre", "apellido", "correo_electronico", "telefono", "password"]

    # Funcion clean() validar campos
    def clean_confirm_pwd(
        self,
    ):  # funciona con el clean() solo, pero no mestra los errores, clena_password() confirm_pwd=None
        cleaned_data = super(RegistroForms, self).clean()

        password = cleaned_data.get("password")
        confirmar_password = cleaned_data.get("confirm_pwd")

        print(f"Registro: password {password} confirmar_password: {confirmar_password}")

        # Validamos si las dos contraseñas conciden
        if password != confirmar_password:
            raise forms.ValidationError("Las contraseñas no coinciden")
            # raise self.add_error('Las contraseñas no coinciden')

        return password

        """ 
        # ! Corregir solo valida la primer validacion que hay en la funcion 

            if len(password) < 5:
            raise forms.ValidationError(
                "La contraseña debe tener como minimo 5 caracteres"
            )

        if not re.search("[0-9]", password):
            raise forms.ValidationError("La contraseña debe tener al menos un número")

        if not re.search(["a-z"], password):
            raise forms.ValidationError(
                "La contraseña debe tener al menos una minúscula"
            )

        if not re.search(["A-Z"], password):
            raise forms.ValidationError(
                "La contraseña debe tener al menos una mayúscula"
            )
        
        """

    # !! Corregir
    """
    def clean_correo(self):
        correo_electronico = self.cleaned_data.get("correo_electronico")

        print(f"Correo: {correo_electronico}")

        # Convertir el correo a minusculas
        correo_electronico = correo_electronico.lower()

        # Devuelve true si la cadena termina con un valor en expecifico
        if correo_electronico.endswith("@gmail.com"):
            raise forms.ValidationError(
                "La dirección de correo electrónico no termina en gmail.com"
            )

        return correo_electronico      
   """

    def clean_telefono(self):
        # Validacion telefono
        telefono = self.cleaned_data.get("telefono")

        # if telefono is not None:
        if not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe tener solo números")

        if len(telefono) < 8 or len(telefono) > 10:
            raise forms.ValidationError(
                "El número de teléfono debe tener entre 8 y 10 dígitos"
            )

        return telefono

    # ? No se esta utilizando
    # el método __init__ se utiliza para ajustar la apariencia y comportamiento
    # de los campos del formulario según las necesidades específicas de diseño de tu aplicación

    def __init__(self, *args, **kwargs):
        super(RegistroForms, self).__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs["placeholder"] = "Ingrese su nombre"
        self.fields["apellido"].widget.attrs["placeholder"] = "Ingrese su apellido"
        self.fields["correo_electronico"].widget.attrs[
            "placeholder"
        ] = "Dirección correo electrónico"
        self.fields["telefono"].widget.attrs["placeholder"] = "Numero telefónico"

        # Se itera para que cada campo tenga la misma clase
        for field in self.fields:
            self.fields[field].widget.attrs[
                "class"
            ] = "form-control"

"""
!HACER VALIDACIONES

- NOMBRE & APELLIDO: mas de 3 palabras

- EMAIL: 
-Permitir solo minusculas
- Validacion que termine en @gmail.com
"""
