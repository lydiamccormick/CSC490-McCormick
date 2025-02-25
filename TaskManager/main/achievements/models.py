from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Achievement(models.Model):
    VALUE_AWARDS = [(i, str(i)) for i in range(1, 6)]
    title = models.CharField(max_length=255)
    badgetype = models.TextField(blank=True, null=True)
    earned = models.BooleanField(default=False)
    earned_on = models.DateTimeField(auto_now_add=True)
    value = models.PositiveIntegerField(choices=VALUE_AWARDS, default = 3)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="achievements")

    def __str__(self):
        return f"{self.title} (Priority: {self.value})"

    def __str__(self):
        return self.title
