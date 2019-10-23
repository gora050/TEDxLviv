from django.db import models
from django.core.files.storage import FileSystemStorage
from event.models import Event
# Create your models here.

fs = FileSystemStorage(location='media/photos')

class Speaker(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    topic = models.CharField(max_length=500)
    description = models.TextField()
    photo = models.ImageField(storage=fs)
    video_link = models.URLField(blank=True)
    event = models.ForeignKey(Event,on_delete=models.CASCADE, related_name="speakers")

    def __str__(self):
        return f"{self.name} {self.surname} - {self.event.name}"