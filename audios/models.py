from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.
class Audios(models.Model):
    titulo = models.CharField(max_length=100)
    audio = models.FileField(upload_to="audios",storage=RawMediaCloudinaryStorage())
    created = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Audio"
        verbose_name_plural = "Audios"
    
    def __str__(self):
        return self.titulo