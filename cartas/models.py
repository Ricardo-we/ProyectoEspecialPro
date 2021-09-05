from django.db import models

# Create your models here.
class Cartas(models.Model):
    titulo = models.CharField(max_length=60)
    contenido = models.TextField()
    final = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Carta"
        verbose_name_plural = "Cartas"

    def __str__(self):
        return self.titulo