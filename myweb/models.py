from django.db import models

class Story(models.Model):
    StoryID = models.IntegerField(primary_key= True, unique=True, auto_created=True)
    StoryName = models.CharField(max_length=250)
    Story_Article = models.TextField(max_length=999999)

class GroupManager(models.Model):
    GroupID = models.IntegerField(primary_key= True, unique=True, auto_created=True)
    Phone = models.CharField(max_length=20, default=None)
    Nickname = models.CharField(max_length=20)

class Writer(models.Model):
    WriterID = models.IntegerField(primary_key= True, unique=True, auto_created=True)
    GID = models.ForeignKey(GroupManager, to_field='GroupID', on_delete=models.CASCADE)
    Name = models.CharField(max_length = 250)
    BIO = models.CharField(max_length = 250)

class StoryElements(models.Model):
    SID = models.ForeignKey(Story, to_field='StoryID', on_delete=models.CASCADE)
    WID = models.ForeignKey(Writer, to_field='WriterID', on_delete=models.CASCADE)
    Story_Type = models.CharField(max_length=150)
    Date_Created = models.CharField(max_length=150)