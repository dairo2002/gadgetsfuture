from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    # Ruta de la categoria
    def get_url_categoria(self):
        return reverse("categoria_a_producto", args=[self.slug])

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    descripcion = models.TextField(max_length=500, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos/")
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def get_url_producto(self):
        return reverse("detalle_producto", args=[self.categoria.slug, self.slug])

    
    # TODO Explicacion

    # ? Metodos get_url_categoria y get_url_producto
    # categoria_a_producto es el nombre de la URL, de la categoria
    # con el slug pasamos el id, pero es mostrado en texto
    # def get_url_categoria(self):
    # path("categoria/<slug:categoria_slug>", views.lista_categoria, name="categoria_a_producto"),
    # return reverse('categoria_a_producto', args=[self.slug])
