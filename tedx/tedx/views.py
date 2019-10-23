from django.shortcuts import render
from event.models import Event

# Create your views here.
def landing_page(request):

    events = Event.objects.all()
    return  render(request,'index1.html',
                   {
        "events" : events
    })