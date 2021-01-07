from django.db import models
from uuid import uuid4
from os import path

class Events(models.Model):
    def get_event_photo(self,filename):
        ext = filename.split(".")[-1]
        filename = f"{uuid4()}.{ext}"
        return path.join("images/event", filename)
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=500)
    photo = models.ImageField(upload_to=get_event_photo)