from django.contrib import admin
from .models import PartnerGroup

# Register your models here.

class PartnerGroupAdmin(admin.ModelAdmin):
    list_editable = ('size_1', 'size_2', 'size_3','order')
    list_display = ('name','event', 'size_1', 'size_2', 'size_3','order')


# Register your models here.
admin.site.register(PartnerGroup, PartnerGroupAdmin)
