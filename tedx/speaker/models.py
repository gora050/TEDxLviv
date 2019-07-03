from django.db import models
from event.models import Event
# Create your models here.

class Speaker(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    topic = models.CharField(max_length=500)
    description = models.TextField()
    photo = models.ImageField()
    video_link = models.URLField(blank=True)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)