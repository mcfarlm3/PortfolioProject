from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    weburl = models.URLField()
    source = models.URLField()


    def __str__(self):
        return self.title

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    start_year = models.SmallIntegerField(null=True)
    end_year = models.SmallIntegerField(null=True)
    location = models.TextField(null=True)

    def __str__(self):
        return self.title
