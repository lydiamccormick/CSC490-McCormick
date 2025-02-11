from django.shortcuts import render

from ics import Calendar, Event
from django.http import HttpResponse
from .models import Task

def generate_ics(request):
    calendar = Calendar()
    
    for task in Task.objects.all():
        if task.deadline:
            event = Event()
            event.name = task.title
            event.begin = task.deadline
            event.description = task.description
            calendar.events.add(event)

    response = HttpResponse(str(calendar), content_type="text/calendar")
    response['Content-Disposition'] = 'attachment; filename="tasks.ics"'
    return response 

