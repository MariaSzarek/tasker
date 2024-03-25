from django.db import models
from django.contrib.auth.models import User


class Task_todo(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('ABANDONED', 'Abandoned'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_tasks', default='')

    def __str__(self):
        return f"{self.title} -{self.status}"
