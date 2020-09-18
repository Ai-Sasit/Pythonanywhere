from django.db import models

class Story(models.Model):
    StoryID = models.IntegerField(primary_key= True, unique=True, auto_created=True)
    StoryName = models.CharField(max_length=250)
    Story_Article = models.TextField(max_length=999999)

class GroupManager(models.Model):
    GroupID = models.IntegerField(primary_key= True, unique=True, auto_created=True)
    Username = models.CharField(max_length=250)
    Password = models.CharField(max_length=250)
    Role = models.CharField(max_length=50)

class Writer(models.Model):
    GID = models.ForeignKey(GroupManager, on_delete=models.CASCADE, default=0)
    WriterID = models.IntegerField(primary_key= True, unique=True, auto_created=True)
    Name = models.CharField(max_length = 250)
    BIO = models.CharField(max_length = 250)

class StoryElements(models.Model):
    SID = models.ForeignKey(Story, on_delete=models.CASCADE)
    WID = models.ForeignKey(Writer, on_delete=models.CASCADE)
    Story_Type = models.CharField(max_length=150)
    Story_category = models.CharField(max_length=150)