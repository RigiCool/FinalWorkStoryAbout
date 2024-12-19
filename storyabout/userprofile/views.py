from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import UserStoryProgress
from .forms import CustomUserChangeForm

# View user profilewith necessary and not secret data
@login_required
def profile_view(request):
    user_progress = UserStoryProgress.objects.filter(user=request.user, read=True)
    data = {
        'user_progress': user_progress,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    }
    return render(request, 'userprofile/profile.html', data)


# View to edit user profile (edit firstname, lastname, username)
@login_required
def edit_profile_view(request):
    
    # Bind the current user's data to the form
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():  # Validate form input
            form.save()  # Save form
            return redirect('userprofile:profile')
    else:
        # Pre-fill the form with the current user's data
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'userprofile/edit.html', {'form': form})


# View to delete user profile
@login_required
def delete_profile_view(request):
    user = request.user
    user.delete() # Delete user
    logout(request) # Logout from current user 
    return redirect('registrationlogin:login') # Redirect to login in view


