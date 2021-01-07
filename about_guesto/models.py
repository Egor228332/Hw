from django.db import models
from uuid import uuid4
from os import path

class History(models.Model):

    text = models.CharField(max_length=500,null=True)

