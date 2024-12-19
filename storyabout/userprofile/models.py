from django.db import models
from django.contrib.auth import get_user_model
from story.models import Story

User = get_user_model()

# Model to track the user's reading progress for each story
class UserStoryProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.story.title} - Read: {self.read}"
