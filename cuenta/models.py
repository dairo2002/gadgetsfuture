from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class ManejardorCuenta(BaseUserManager):
    def create_user(self, nombre, apellido, usuario, correo_electronico, password=None):
        if not correo_electronico:
            raise ValueError(
                "El usuario debe tener una dirección de correo electrónico"
            )
        if not usuario:
            raise ValueError("El usuario debe tener un nombre de usuario")
        
        # Crear un objeto de usuario con datos normalizados
        usuarios = self.model(
            # normalize_email Convierte la direccion de correo a minusculas y elimina espacios
            correo_electronico=self.normalize_email(correo_electronico),
            usuario=usuario,
            nombre=nombre,
            apellido=apellido,
        )

        # Establecer la contraseña y guardar el usuario en la base de datos
        usuarios.set_password(password)
        usuarios.save(using=self._db)
        return usuarios

    # Método para crear un superusuario con privilegios especiales
    def create_superuser(self, nombre, apellido, usuario, correo_electronico, password):
         # Utilizar el método create_user para crear un superusuario
        usuarios = self.create_user(
            correo_electronico=self.normalize_email(correo_electronico),
            usuario=usuario,
            password=password,
            nombre=nombre,
            apellido=apellido,
        )

        # Establecer permisos y características especiales para el superusuario
        usuarios.administrador = True
        usuarios.personal = True
        usuarios.activo = True
        usuarios.super_administrador = True
        usuarios.save(using=self._db)
        return usuarios


# Creamos el modelo de usuario personalizado que hereda de AbstractBaseUser
class Cuenta(AbstractBaseUser):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    # username
    usuario = models.CharField(max_length=50, unique=True)
    correo_electronico = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=50)

    # Permisos campos requeridos
    inicio_acceso = models.DateField(auto_now_add=True)
    ultimo_acceso = models.DateField(auto_now_add=True)
    administrador = models.BooleanField(default=False)
    personal = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    super_administrador = models.BooleanField(default=False)

    # Campo con el que debe iniciar sesion el administrador
    USERNAME_FIELD = "correo_electronico"
    # Campos requeridos obligatorios ademas del correo y contraseña cuando se crea un usuario, atraves del comando createsuperuser
    REQUIRED_FIELDS = ["nombre", "apellido", "usuario"]
    # Utilizamos el manejador de usuarios personalizado
    objects = ManejardorCuenta()

    def __str__(self):
        return self.correo_electronico

    def has_perm(self, perm, obj=None):
        return self.administrador

    def has_module_perms(self, app_label):
        return True


# ? Por ultimo, Configurar el modelo de cuenta el settings.py
