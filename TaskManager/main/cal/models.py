# from django.db import models
# from tasks.models import Task

# class CalendarDate(models.Model):
#     task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="calendar_events")
#     due_date = models.DateTimeField() 
#     title = models.CharField(max_length=255) 
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.title
