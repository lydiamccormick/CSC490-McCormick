from django.shortcuts import render, redirect

from ics import Calendar, Event
from django.http import HttpResponse
from django.template import loader
from .models import Task
from .forms import TaskForm

def tasks(request):
  mytasks = Task.objects.all().values()
  template = loader.get_template('all_tasks.html')
  context = {
    'mytasks': mytasks,
  }
  return HttpResponse(template.render(context, request))

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

def new(request):
    if request.method == "POST":
      form = TaskForm(request.POST)
      form.save()
      return redirect("/")
    else:
       form = TaskForm()
    return render(request, "tasks/new.html", {"form": form})