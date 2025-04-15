"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views
from members.views import signup
from members.views import signin
from members.views import signout
from cal.views import calendar
from tasks.views import new, delete

urlpatterns = [
    path('', views.home, name = 'home'),
    path("admin/", admin.site.urls),
    path("home/", views.dashboard, name = 'dashboard'),
    path("members/", views.members, name='members'),
    path("newuser/", signup, name='newuser'),
    path("currentuser/", signin, name='currentuser'),
    path("logout/", signout, name = 'logout'),
    path("tasks/", include('tasks.urls')),
    path("achievements/", include('achievements.urls')),
    path('calendar/', include('cal.urls'))
]

