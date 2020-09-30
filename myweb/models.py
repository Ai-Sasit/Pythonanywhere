from django.conf import settings
from django.db import models

class GroupManager(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    GroupID = models.AutoField(primary_key= True, unique=True, auto_created=True)
    Phone = models.CharField(max_length=20)
    Nickname = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.GroupID} - {self.Nickname}"

class Writer(models.Model):
    GID = models.ForeignKey(GroupManager, to_field='GroupID', on_delete=models.CASCADE)
    Name = models.CharField(primary_key=True, max_length = 250)
    BIO = models.CharField(max_length = 250)

    def __str__(self):
        return f"{self.Name}"

class StoryElements(models.Model):
    SID = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    WID = models.ForeignKey(Writer, to_field='Name', on_delete=models.CASCADE)
    StoryName = models.CharField(max_length=250)
    Story_Type = models.CharField(max_length=150)
    Date_Created = models.DateTimeField(auto_now_add=True)
    AutoDate = models.CharField(max_length=100, default=None)

    def __str__(self):
        return f"{self.SID} - {self.StoryName}"

class Story(models.Model):
    StoryID = models.OneToOneField(StoryElements, to_field="SID" , on_delete=models.CASCADE,primary_key=True)
    Story_Article = models.TextField(max_length=999999)

    def __str__(self):
        return f"Story ID: {self.StoryID}"