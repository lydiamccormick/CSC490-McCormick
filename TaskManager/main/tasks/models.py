from django.db import models
from cal.models import CalendarDate
from django.contrib.auth.models import User

class Task(models.Model):
    VALUE_CHOICES = [(i, str(i)) for i in range(1, 6)]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    value = models.PositiveIntegerField(choices=VALUE_CHOICES, default = 3)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    calendar_date = models.ForeignKey(CalendarDate, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')


    def __str__(self):
        return f"{self.title} (Priority: {self.value})"

class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    tasks = models.ManyToManyField(Task, related_name="categories", blank=True)

    def __str__(self): 
        return self.name

