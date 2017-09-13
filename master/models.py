from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=64)
