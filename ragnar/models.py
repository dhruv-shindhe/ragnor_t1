from django.db import models

# Create your models here.

class Quotes(models.Model):
    text = models.CharField(max_length=1000)
    author = models.CharField(max_length=20)
