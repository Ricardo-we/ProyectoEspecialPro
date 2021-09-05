from django.db import models

# Create your models here.
class Fotos(models.Model):
    titulo = models.CharField(max_length=150)
    foto = models.ImageField(upload_to="fotos")
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"

