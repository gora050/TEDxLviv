from django.contrib import admin
from .models import Event
from partner_group.models import PartnerGroup

# Register your models here.

class PartnerGroupInline(admin.TabularInline):
    model = PartnerGroup

class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['name', 'title', ]
    inlines = [
        PartnerGroupInline,
    ]

admin.site.register(Event, EventAdmin)
# Register your models here.