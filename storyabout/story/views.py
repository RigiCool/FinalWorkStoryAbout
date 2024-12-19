from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms import modelformset_factory
from .forms import StoryForm, StoryFrameForm
from .models import Story, StoryFrame
from userprofile.models import UserStoryProgress
import os
from django.conf import settings


# Check if user is an admin (superuser or staff)
def admin_required(user):
    return user.is_staff or user.is_superuser



# View to create a new story
@login_required
@user_passes_test(admin_required)
def create_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save() # Save valid form
            return redirect('story:add_frame', story_id=story.id)  # Redirect to add frames after creating the story
    else:
        form = StoryForm()
    return render(request, 'story/create_story.html', {'form': form})



# View to add a frame (chapter) to a story
@login_required
@user_passes_test(admin_required)
def add_frame(request, story_id):
    # Retrieve the story by its ID
    story = get_object_or_404(Story, id=story_id)
    if request.method == 'POST':
        form = StoryFrameForm(request.POST, request.FILES)
        if form.is_valid():
            frame = form.save(commit=False)
            frame.story = story  # Associate the frame with the story
            frame.save() # Save story
            return redirect('story:story_details', story_id=story.id)  # Redirect to story detail after adding the frame
    else:
        form = StoryFrameForm()
    return render(request, 'story/add_frame.html', {'form': form, 'story': story})


# View to edit a frame (chapter) to a story
@login_required
@user_passes_test(admin_required)
def edit_frame(request, story_id, frame_id):
    # Retrieve the story by its ID
    story = get_object_or_404(Story, id=story_id)
    frame = get_object_or_404(StoryFrame, id=frame_id, story=story)

    if request.method == 'POST':
        form = StoryFrameForm(request.POST, request.FILES, instance=frame)
        if form.is_valid():
            form.save()
            return redirect('story:story_details', story_id=story.id)
    else:
        form = StoryFrameForm(instance=frame)

    return render(request, 'story/edit_frame.html', {'form': form, 'story': story})


# View to delete a story
def delete_story(request, story_id):
    # Retrieve the story by its ID
    story = get_object_or_404(Story, id=story_id)

    # Delete associated images from StoryFrame
    for frame in story.frames.all():
        if frame.image:
            file_path = os.path.join(settings.MEDIA_ROOT, frame.image.name)
            if os.path.isfile(file_path):
                os.remove(file_path)

    # Check and delete the background image of the story
    if story.background_image:
        background_file_path = os.path.join(settings.MEDIA_ROOT, story.background_image.name)
        if os.path.isfile(background_file_path):
            os.remove(background_file_path)

    story.delete()

    # Retrieve all stories to render the updated list
    stories = Story.objects.all()
    return render(request, 'story/stories.html', {'stories': stories})



# View to open a story details (the view with frames of current story)
@login_required
def story_detail(request, story_id):
    # Retrieve the story by its ID
    story = get_object_or_404(Story, id=story_id)

    # Get all the associated frames (chapters) for this story
    frames = story.frames.all()  # Collect all story frames of current story

    progress = UserStoryProgress.objects.filter(user=request.user, story=story).first()

    user_has_read_story = progress.read if progress else False

    # Pass the story and its frames to the template
    return render(request, 'story/story_details.html', {'story': story, 'frames': frames, 'user_has_read_story': user_has_read_story})



# View to mark the story as completed for current user
@login_required
def mark_as_read(request, story_id):
    # Retrieve the story by its ID
    story = get_object_or_404(Story, id=story_id)
    progress, created = UserStoryProgress.objects.get_or_create(user=request.user, story=story)

    # Toggle the read status
    progress.read = not progress.read
    progress.save()

    return redirect('story:stories')

# View to go back to all stories
@login_required
def stories(request):
    stories = Story.objects.all()

    return render(request, 'story/stories.html', {'stories': stories})
