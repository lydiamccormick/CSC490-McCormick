from django.shortcuts import render
from django.utils.timezone import localtime
from datetime import datetime, timedelta
from tasks.models import Task

def calendar_month_view(request, year, month):
    first_day_of_month = datetime(year, month, 1)
    last_day_of_month = datetime(year, month + 1, 1) - timedelta(days=1)

    tasks_for_month = Task.objects.filter(due_date__gte=first_day_of_month, due_date__lte=last_day_of_month)

    task_by_day = {}
    for task in tasks_for_month:
        task_date = task.due_date.date()
        if task_date not in task_by_day:
            task_by_day[task_date] = []
        task_by_day[task_date].append(task)

    return render(request, 'calendar/calendar_month.html', {
        'year': year,
        'month': month,
        'task_by_day': task_by_day,
    })
