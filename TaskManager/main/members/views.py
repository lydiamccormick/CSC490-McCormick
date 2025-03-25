from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Member
from datetime import datetime
from .forms import CreateAccount
from .forms import SignIn
from django.contrib.auth import authenticate, login
from django.contrib import messages

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request)) 

def signup(request):
    if request.method == "POST":
        form = CreateAccount(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            new_user = authenticate(username=username, 
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            messages.success(request, f'Account created for {username}')
            return redirect("/")
    else:
        form = CreateAccount()
    return render(request, "newuser/signup.html", {"form": form})

def signin(request):
    if request.method == "POST":
        form = SignIn(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = SignIn()
    
    return render(request, "currentuser/signin.html", {"form": form})

