from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100, unique=False)
    event = models.CharField(max_length=100, blank=True)
    about = models.CharField(max_length=300, blank=True)
    created_at = models.DateField(auto_now_add=True)
