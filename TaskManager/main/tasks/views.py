from django.shortcuts import render, redirect, get_object_or_404
from ics import Calendar, Event
from django.http import HttpResponse
from django.template import loader
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required



@login_required
def tasks(request):
    mytasks = Task.objects.filter(user=request.user)
    return render(request, 'all_tasks.html', {'mytasks': mytasks})

# def generate_ics(request):
#     calendar = Calendar()
    
#     for task in Task.objects.all():
#         if task.deadline:
#             event = Event()
#             event.name = task.title
#             event.begin = task.deadline
#             event.description = task.description
#             calendar.events.add(event)

#     response = HttpResponse(str(calendar), content_type="text/calendar")
#     response['Content-Disposition'] = 'attachment; filename="tasks.ics"'
#     return response 

@login_required
def new(request):
    if request.method == "POST":
      form = TaskForm(request.POST)
      if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
      return redirect("/tasks")
    else:
       form = TaskForm()
    return render(request, "newtasks/new.html", {"form": form}) 

@login_required
def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:index')
    return redirect('tasks:index') 

@login_required
def complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = True
    task.save()
    return redirect('tasks:index')

