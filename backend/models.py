from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=200)
    count = models.IntegerField()
