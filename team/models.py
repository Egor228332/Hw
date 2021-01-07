from django.db import models

class Team(models.Model):
    description = models.CharField(max_length=500,unique=True)
