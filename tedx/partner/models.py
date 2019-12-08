from django.db import models
from django.core.files.storage import FileSystemStorage
from event.models import Event

# Create your models here.

fs = FileSystemStorage(location='media/photos')


class Partner(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(storage=fs)
    link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} "
