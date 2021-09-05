from django.db import models

# Create your models here.
class Updates(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()

    class Meta:
        verbose_name = "Update"
        verbose_name_plural = "Updates"

class Downloads(models.Model):
    titulo = models.CharField(max_length=60)
    archivo = models.FileField(upload_to="descargas")
    descripcion = models.TextField(max_length=250)

    class Meta:
        verbose_name = "Download"
        verbose_name_plural = "Downloads"
