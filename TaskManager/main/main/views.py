from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from members.models import Member
from tasks.models import Task
from achievements.models import Achievement
from cal.models import CalendarDate
from django.contrib.auth.decorators import login_required


def home(request):
    task_count = 0

    if request.user.is_authenticated:
        task_count = Task.objects.filter(
            user=request.user,
            completed=False
        ).count()
    task_list = []
    task_list_completed = []
    if request.user.is_authenticated:
       task_list = Task.objects.filter(
          user=request.user,
          completed=False
       )
    if request.user.is_authenticated:
       task_list_completed = Task.objects.filter(
          user=request.user,
          completed=True
       )
  
    return render(request, 'home.html', {
        'task_count': task_count,
        'task_list': task_list,
        'task_list_completed': task_list_completed,
    }) 

def dashboard(request):
    return render(request, 'home.html') 

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

@login_required(login_url="/currentuser")
def tasks(request):
  mytasks = Task.objects.filter(user=request.user)
  template = loader.get_template('all_tasks.html')
  context = {
    'mytasks': mytasks,
  }
  return HttpResponse(template.render(context, request))

def achievements(request):
  myachievements = Achievement.objects.all().values()
  template = loader.get_template('all_achievements.html')
  context = {
    'myachievements': myachievements,
  }
  return HttpResponse(template.render(context, request))

@login_required
def calendar(request):
    return render(request, 'calendar.html')
