from django.db import models

class Booking(models.Model):
    number = models.CharField(max_length=15)
