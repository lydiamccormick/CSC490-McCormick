from django.urls import path
from . import views

#URLConfiguration
urlpatterns = [
    path('hello/', views.say_hello),
    path('welcome/', views.welcome_message),
    path('dashboard/', views.dashboard)
]