import re
from django import forms
from .models import Story, StoryFrame
from django.forms import TextInput, Textarea, ClearableFileInput, NumberInput
from django.core.exceptions import ValidationError

# Story form
class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = [
            'title', 'author', 'background_image',
        ]

        widgets = {
            "background_image": ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            "title": TextInput(attrs={
                'class': 'form-control',
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
            }),
        }
        
    # Title field verification
    def clean_title(self):
        title = self.cleaned_data.get('title', '')

        if len(title) < 3:
            raise ValidationError("Title must contain at least 3 characters.")
        elif len(title) > 30:
            raise ValidationError("Title must contain less then 30 characters.")
        if not title[0].isupper():
            raise ValidationError("Title should start with a capital letter.")
        if not any(char.isalpha() for char in title):
            raise ValidationError("Title must contain at least one letter.")
        if not re.match(r"^[A-Za-z0-9\s.,?!']+$", title):
            raise ValidationError("Title contains invalid characters. Use only letters, numbers, spaces, and basic punctuation.")
        return title

    # Author field verification
    def clean_author(self):
        author = self.cleaned_data.get('author', '')

        if not author[0].isupper():
            raise ValidationError("Author should start with a capital letter.")
        if len(author) < 3:
            raise ValidationError("Author must contain at least 3 characters.")
        elif len(author) > 40:
            raise ValidationError("Author must contain less then 40 characters.")
        if not re.match(r"^[A-Za-z0-9\s.,?!']+$", author):
            raise ValidationError("Author contains invalid characters. Use only letters, numbers, spaces, and basic punctuation.")
        return author

# Story frame form
class StoryFrameForm(forms.ModelForm):
    class Meta:
        model = StoryFrame
        fields = ['chapter', 'paragraph', 'image', 'position']

        widgets = {
            "chapter": NumberInput(attrs={
                'class': 'form-control',
            }),
            "image": ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            "paragraph": Textarea(attrs={
                'class': 'form-control',
                'rows': 20,
            }),
            "position": TextInput(attrs={
                'class': 'form-control',
            }),
        }
    # Paragraph field verification
    def clean_paragraph(self):
        paragraph = self.cleaned_data.get('paragraph', '')
        if paragraph:
            stripped_paragraph = paragraph.replace(" ", "")
            
            num_letters = sum(c.isalpha() for c in stripped_paragraph)
            num_numbers = sum(c.isdigit() for c in stripped_paragraph)
            if len(paragraph) < 80:
                raise ValidationError("Title must contain at least 20 characters.")
            elif len(paragraph) > 2000:
                raise ValidationError("Title must contain less then 30 characters.")
            if num_letters <= num_numbers:
                raise ValidationError("The paragraph must contain more letters than numbers.")
            # if not re.match(r"^[A-Za-z0-9\s.,?!']+$", paragraph):
            #     raise ValidationError("The paragraph contains invalid characters. Use only letters, numbers, spaces, and basic punctuation.")
            if not paragraph[0].isupper():
                raise ValidationError("The paragraph should start with a capital letter.")
        return paragraph

    # Custom position choice field with options
    POSITION_CHOICES = [
        ('left', 'Left'),
        ('center', 'Center'),
        ('right', 'Right'),
    ]
    position = forms.ChoiceField(choices=POSITION_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control',
        'placeholder': 'Position',
    }))
