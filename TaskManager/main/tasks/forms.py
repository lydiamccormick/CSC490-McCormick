from .models import Task
from django.forms import ModelForm, Textarea
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user', 'completed']  
        widgets = {
            'description': Textarea()
        } 



