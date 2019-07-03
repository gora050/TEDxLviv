from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    date = models.DateTimeField()
    place = models.CharField(max_length=500)
    description = models.TextField()
    photo = models.ImageField()
    tickets_link = models.URLField(blank=True)

