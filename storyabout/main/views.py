from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Render the page only for authenticated users.
@login_required
def index(request):
    return render(request, 'main/index.html')
