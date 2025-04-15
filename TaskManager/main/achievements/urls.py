from django.urls import path
from . import views
from members.views import signin

urlpatterns = [
    path('signin/',signin, name = 'signin'),
    path('', views.achievements, name='achievements'),
]