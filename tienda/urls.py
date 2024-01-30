from django.urls import path, include
from . import views

urlpatterns = [        
    path("", views.tienda, name="tienda"),
    # Esta ruta muestra los productos que pertenecen a una categoria
    path("categoria/<slug:categoria_slug>/", views.tienda, name="categoria_a_producto"),
    # Ruta de una categoria de un producto, que va hacia el detelle del producto
    path('categoria/<slug:categoria_slug>/<slug:producto_slug>/', views.detalle_producto, name='detalle_producto'),
    # Ruta busqueda de un producto
    path("buscar/", views.buscar_producto, name="buscar_producto"),

        
]
