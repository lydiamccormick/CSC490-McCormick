from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from cal.models import CalendarDate



@login_required(login_url = "signin/")
def tasks(request):
    mytasks = Task.objects.filter(user=request.user)
    return render(request, 'all_tasks.html', {'mytasks': mytasks})


@login_required
def new(request):
    if request.method == "POST":
      form = TaskForm(request.POST)
      if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            due_date = task.due_date.date() if task.due_date else None
            if due_date:
                calendar_date, created = CalendarDate.objects.get_or_create(date=due_date)
                task.calendar_date = calendar_date  
            task.save()
      return redirect("/tasks")
    else:
       form = TaskForm()
    return render(request, "newtasks/new.html", {"form": form}) 

@login_required
def new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Set the logged-in user

            # Assuming the 'due_date' is provided in the form (or you can use another logic)
            due_date = task.due_date.date() if task.due_date else None

            if due_date:
                # Find or create the CalendarDate for the given due_date
                calendar_date, created = CalendarDate.objects.get_or_create(date=due_date)
                task.calendar_date = calendar_date  # Link the task to the CalendarDate
            
            task.save()  # Save the task with the assigned calendar_date
            return redirect("/tasks")  # Redirect after saving the task
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


