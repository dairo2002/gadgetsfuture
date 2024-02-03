from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cuenta


class CuentaAdmin(UserAdmin):
    list_display = (
        "correo_electronico",
        "nombre",
        "apellido",        
        "username",
        "inicio_acceso",
        "ultimo_acceso",
        "is_active",
        "is_admin",
    )

    ordering = ["correo_electronico"]
    # Campos con link
    list_display_links = ("correo_electronico", "username")
    # Campos solo lectura
    readonly_fields = ("inicio_acceso", "ultimo_acceso")
    # Filtro horizontal
    filter_horizontal = ()
    list_filter = ["is_active", "is_superadmin"]
    # fieldsets = (
    #     ("informacion Personal", {"fields": ("nombre", "apellido", "correo_electronico", "usuario", 'telefono')}),
    #     ("Permisos", {"fields": ("is_admin", "is_active", "is_staff", "is_superadmin")}),
    # )
    fieldsets = ()

admin.site.register(Cuenta, CuentaAdmin)


# class AccountAdmin(UserAdmin):
#     list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
#     list_display_links = ('email', 'first_name', 'last_name')
#     readonly_fields = ('last_login', 'date_joined')
#     ordering = ('-date_joined',)

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()

# admin.site.register(Account, AccountAdmin)
