from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .models import CalendarDate


@login_required(login_url = "signin/")
def calendar(request):
    return render(request, 'calendar.html')

def calendar_data(request):
    user = request.user
    cal_entries = CalendarDate.objects.prefetch_related('tasks').all()
    data = []
    for entry in cal_entries:
        task_list = []
        user_tasks = entry.tasks.filter(user=user)
        for task in user_tasks:
            if task.completed:
                color = 'green'
            elif task.due_date and (task.due_date + timedelta(days=1)) <= timezone.now():
                color = 'red'
            else:
                color = 'yellow'
            task_list.append({
                'title': task.title,
                'priority': task.value,
                'due_date': task.due_date.isoformat() if task.due_date else None,
                'color': color,
            })
        data.append({
            'date': entry.date.isoformat(),
            'tasks': task_list
        })
    return JsonResponse(data, safe=False)
