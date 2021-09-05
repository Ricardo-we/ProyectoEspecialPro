from django.db import models

# Create your models here.
class Audios(models.Model):
    titulo = models.CharField(max_length=100)
    audio = models.FileField(upload_to="audios")
    created = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Audio"
        verbose_name_plural = "Audios"
    
    def __str__(self):
        return self.titulo