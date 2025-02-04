from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action

def say_hello(request):
    # pull data from db, transform, send email, etc
    return render(request, 'hello.html')

def welcome_message(request):
    return HttpResponse('Welcome to My Website') 

def dashboard(request):
    return render(request, 'task_client.html')
