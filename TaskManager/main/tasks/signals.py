from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from achievements.models import Achievement


@receiver(post_save, sender=Task)
def award_achievement(sender, instance, created, **kwargs):
    return

@receiver(post_save, sender=Task)
def award_first_task_achievement(sender, instance, created, **kwargs):
    if instance.completed:
        achievement, _ = Achievement.objects.get_or_create(
            name="First Task Completed",
            defaults={"description": "Completed your very first task!"}
        )
        if not instance.user.achievements.filter(id=achievement.id).exists():
            instance.user.achievements.add(achievement)

