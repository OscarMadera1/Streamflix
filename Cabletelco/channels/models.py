# Create your models here.
from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField()
    stream_url = models.URLField()

    def __str__(self):
        return self.name
