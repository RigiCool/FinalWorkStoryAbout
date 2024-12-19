from django.urls import path
from . import views

app_name = 'story'

urlpatterns = [
    path('create-story/', views.create_story, name='create_story'),
    path('add-frame/<int:story_id>/', views.add_frame, name='add_frame'),
    path('delete-story/<int:story_id>/', views.delete_story, name='delete_story'),
    path('story/<int:story_id>/', views.story_detail, name='story_details'),
    path('stories/', views.stories, name='stories'),
    path('mark-as-read/<int:story_id>/', views.mark_as_read, name='mark_as_read'),
    path('edit_frame/<int:story_id>/<int:frame_id>/', views.edit_frame, name='edit_frame'),
]
