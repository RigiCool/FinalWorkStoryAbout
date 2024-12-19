from django.contrib import admin
from . models import UserStoryProgress

# Register user story progress model. (Progress - list of books read)
admin.site.register(UserStoryProgress)
