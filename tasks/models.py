from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.timezone import now


class Task(models.Model):
    PRIORITY_CHOICES = (
        ('1', '😍'),
        ('2', '😍😍'),
        ('3', '😍😍😍'),
    )
    done = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    attributed_to = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(default=now)
    end_date = models.DateField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)


    def __str__(self):
        return self.title
