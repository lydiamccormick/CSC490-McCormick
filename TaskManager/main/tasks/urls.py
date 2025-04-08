from django.urls import path
from . import views

app_name = 'tasks' 

urlpatterns = [
    path('', views.tasks, name='index'),
    path('new/', views.new, name='new'),
    path('complete/<int:task_id>/', views.complete, name='complete'), 
    path('delete/<int:task_id>/', views.delete, name='delete')
]
