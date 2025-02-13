from django.db import models

# Create your models here.
class Member(models.Model):
    first = models.CharField(max_length=255)
    last  = models.CharField(max_length=255)
    date_joined = models.DateField(null=True)

    def __str__(self):
        return f"{self.first} {self.last}"