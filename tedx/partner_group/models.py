from django.db import models
from django.core.files.storage import FileSystemStorage
from event.models import Event
from partner.models import Partner

# Create your models here.


class PartnerGroup(models.Model):
    name = models.CharField(max_length=50)
    event = models.ForeignKey(Event,on_delete=models.CASCADE, related_name="partnergroups")
    partners = models.ManyToManyField(Partner,
                                           related_name="partnergroups", blank=True,)
    order = models.IntegerField(default=1)
    size_1 = models.IntegerField(default=6)
    size_2 = models.IntegerField(default=3)
    size_3 = models.IntegerField(default=2)

    class Meta:
        ordering = ['order', ]
        
    def __str__(self):
        return f"{self.event.name} {self.name}"