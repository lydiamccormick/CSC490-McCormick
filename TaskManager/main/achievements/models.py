from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task
from django.utils import timezone

class Achievement(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="Completed a task.")
    earned = models.BooleanField(default=False)
    earned_on = models.DateTimeField(default=timezone.now)
    user = models.ManyToManyField(User, related_name='achievements', blank=True)

    def __str__(self):
        return self.name


from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Task)
def check_first_task_completed(sender, instance, created, **kwargs):
    if instance.completed:
        user = instance.user
        first_achievement = Achievement.objects.get(name="First Task Completed")

        # Check how many completed tasks the user has
        completed_count = Task.objects.filter(user=user, completed=True).count()

        # If this is their first completed task and they don’t have the achievement yet
        if completed_count == 1 and not first_achievement.user.filter(id=user.id).exists():
            first_achievement.user.add(user)
            print(f"{user.username} earned their first achievement!")
