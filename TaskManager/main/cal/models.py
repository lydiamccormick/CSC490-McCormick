from django.db import models
from django.utils import timezone

class CalendarDate(models.Model):
    date = models.DateField()

    def __str__(self):
        return f"Calendar Date: {self.date}"

    def get_task_events(self):
        events = []
        for task in self.tasks.all():
            if task.completed:
                color = 'green'
            elif task.due_date and task.due_date < timezone.now():
                color = 'red'
            else:
                color = 'yellow'

            events.append({
                'title': task.title,
                'priority': task.value,
                'color': color,
                'due_date': task.due_date,
            })
        return events

