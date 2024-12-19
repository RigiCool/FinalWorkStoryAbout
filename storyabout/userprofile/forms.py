from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

# User profile edit form
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
        }
    
    # Username field verification
    def clean_username(self):
        username = self.cleaned_data.get('username', '')

        if len(username) < 3:
            raise ValidationError("Username must contain at least 3 characters.")
        elif len(username) > 20:
            raise ValidationError("Username must contain less then 20 characters.")
        if not any(char.isalpha() for char in username):
            raise ValidationError("Username must contain at least one letter.")
        return username
    
    # First name field verification
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name', '')

        if not first_name.isalpha():
            raise ValidationError("First name should contain only letters.")
        if not first_name[0].isupper():
            raise ValidationError("First name should start with a capital letter.")
        if len(first_name) < 3:
            raise ValidationError("First name must contain at least 3 characters.")
        elif len(first_name) > 20:
            raise ValidationError("First name must contain less then 20 characters.")
        return first_name
    
    # Last name field verification
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name', '')
        
        if not last_name.isalpha():
            raise ValidationError("Last name should contain only letters.")
        if not last_name[0].isupper():
            raise ValidationError("Last name should start with a capital letter.")
        if len(last_name) < 3:
            raise ValidationError("First name must contain at least 3 characters.")
        elif len(last_name) > 20:
            raise ValidationError("First name must contain less then 20 characters.")
        return last_name
