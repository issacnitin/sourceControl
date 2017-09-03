from django.db import models
from monoengine import Document, EmbeddedDocument, fields

class EventTable(models.Model):
    id = models.CharField(max_length=140, primary_key=True)
    type = models.CharField(max_length=140)
    actorid = models.CharField(max_length=140)
    repoid = models.CharField(max_length=140)
    payloadid = models.CharField(max_length=140)

    def __str__(self):
        return self.title

class ActorTable(models.Model):
    actorid = models.CharField(max_length=140, primary_key=True)
    login = models.CharField(max_length=140)
    gravatar_id = models.CharField(max_length=140)
    url = models.CharField(max_length=140)
    avatar_url = models.CharField(max_length=140)

    def __str__(self):
        return self.title
    
class RepoTable(models.Model):
    repoid = models.CharField(max_length=140, primary_key=True)
    name = models.CharField(max_length=140)
    url = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.title

class PayloadTable(models.Model):
    pushid = models.CharField(max_length=140, primary_key=True)
    size = models.CharField(max_length=140)
    distinct_size = models.CharField(max_length=140)
    ref = models.CharField(max_length=140)
    head = models.CharField(max_length=140)
    before = models.CharField(max_length=140)
    commitid = models.CharField(max_length=140)
    public = models.CharField(max_length=140)
    created_at = models.CharField(max_length=140)
    
    def __str__(self):
        return self.title

class CommitTable(models.Model):
    actorid = models.CharField(max_length=140)
    sha = models.CharField(max_length=140, primary_key=True)
    email = models.CharField(max_length=140)
    name = models.CharField(max_length=140)
    message = models.CharField(max_length=140)
    distinct = models.CharField(max_length=140)
    url = models.CharField(max_length=140)
    
    def __str__(self):
        return self.title