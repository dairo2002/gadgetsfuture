from django.urls import path

from . import views

urlpatterns = [                        
    path("realizar_pedido", views.realizar_pedido, name='realizar_pedido' ),
]