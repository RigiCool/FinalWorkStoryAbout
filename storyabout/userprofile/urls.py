from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('edit/', views.edit_profile_view, name='edit'),
    path('delete/', views.delete_profile_view, name='delete'),
]
