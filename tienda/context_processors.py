from .models import Categoria

def enlaces_categorias(request):
    # Consultamos todas la categorias
    enlace = Categoria.objects.all()
    # dict=diccionario
    return dict(enlace_categoria=enlace)