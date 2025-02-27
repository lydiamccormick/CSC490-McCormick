from .models import Task
from django.forms import ModelForm, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'description': Textarea()
        }
