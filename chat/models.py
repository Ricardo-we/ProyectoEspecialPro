from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=150)
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Messages(models.Model):
    username = models.CharField(max_length=150)
    message = models.TextField()

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
