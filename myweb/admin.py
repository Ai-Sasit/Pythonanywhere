from django.contrib import admin

from .models import Story, StoryElements, GroupManager, Writer

admin.site.register(Story)
admin.site.register(StoryElements)
admin.site.register(GroupManager)
admin.site.register(Writer)