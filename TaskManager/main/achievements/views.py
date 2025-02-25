from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Achievement

def index(request):
    return HttpResponse("Hello World")

def achievements(request):
  myachievements = Achievement.objects.all().values()
  template = loader.get_template('all_achievements.html')
  context = {
    'myachievements': myachievements,
  }
  return HttpResponse(template.render(context, request))
