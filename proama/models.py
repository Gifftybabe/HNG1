from django.db import models

# Create your models here.


class Info(models.Model):
    slackUsername = models.CharField(max_length=20)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.CharField(max_length=300)
