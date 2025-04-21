from django.shortcuts import render
from tasks.models import Task
from django.utils import timezone

def dashboard_view(request):
    user = request.user
    task_count = Task.objects.filter(
        user=user,
        completed=False,
        due_date__gte=timezone.now()
        ).count()
    
    return render(request, 'home.html', {
        'task_count': task_count,
    })