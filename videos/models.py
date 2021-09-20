from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage,VideoMediaCloudinaryStorage
# Create your models here.
class Videos(models.Model):
    video = models.FileField(upload_to="videos",storage=VideoMediaCloudinaryStorage())
    titulo = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"