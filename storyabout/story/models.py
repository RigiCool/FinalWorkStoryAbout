from django.db import models

# Story model
class Story(models.Model):
    title = models.CharField('Title', max_length=50)
    author = models.CharField('Author', max_length=50)
    background_image = models.ImageField('Background Image', upload_to='backgrounds/', blank=False, null=True)

    def __str__(self):
        return self.title

# Story frame model
class StoryFrame(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='frames')
    chapter = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='slides/', blank=True, null=True)
    paragraph = models.TextField(blank=True, null=True)
    position = models.CharField('Position', max_length=50, blank=True, null=True)  # Ensure position field exists

    def __str__(self):
        return f"Frame {self.chapter} for {self.story.title}"
