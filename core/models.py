from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()
    imagen_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo

class Inicio(models.Model):
    imagen_url = models.URLField(blank=True, null=True)
    titulo = models.CharField(max_length=200, default="Bienvenido a CyberSec")
    descripcion = models.TextField(default="ej: Tu fuente de noticias y herramientas de ciberseguridad.")

    def __str__(self):
        return self.titulo

class Herramienta(models.Model):
    imagen_url = models.URLField(blank=True, null=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.nombre