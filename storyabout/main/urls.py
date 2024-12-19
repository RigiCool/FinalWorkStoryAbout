from django.urls import path
from . import views

# Application name "main"
app_name = 'main'

urlpatterns = [
    path('', views.index, name = 'index')
]
