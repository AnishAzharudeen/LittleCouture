from django.db import models
from django.utils import timezone


class About(models.Model):
    title = models.CharField(max_length=200)
    #updated_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.title