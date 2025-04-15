from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Achievement
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("Hello World")


@login_required(login_url = "signin/")
def achievements(request):
    achievements = Achievement.objects.all()
    user_achievements = request.user.achievements.all()
    context = {
        'achievements': achievements,
        'user_achievements': user_achievements
    }
    return render(request, 'all_achievements.html', context)

