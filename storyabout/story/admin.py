from django.contrib import admin
from . models import Story, StoryFrame

# Register models to database.
admin.site.register(Story)
admin.site.register(StoryFrame)
