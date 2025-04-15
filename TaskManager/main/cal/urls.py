from django.urls import path
from . import views
from members.views import signin

urlpatterns = [
    path('signin/',signin, name = 'signin'),
    path('calendar-data/', views.calendar_data, name='calendar_data'),
    path('', views.calendar, name='calendar'),
]