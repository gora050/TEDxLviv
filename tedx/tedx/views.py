from django.shortcuts import render
from event.models import Event
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
def landing_page(request):

    events = Event.objects.all()
    return  render(request,'index1.html',
                   {
        "events" : events
    })

# Create your views here.
def event(request, event_name):

    events = Event.objects.all()
    event = get_object_or_404(Event,name=event_name)
    return  render(request,'event.html',
                   {
        "main_event" : event,
        "events" : events
    })