from django import forms
from products.widgets import CustomClearableFileInput

from .models import Post


class PostForm(forms.ModelForm):
    """ Form to create an article """
    class Meta:
        model = Post
        fields = ['title', 'content', 'excerpt', 'image']

        labels = {
            'title': 'Article Title',
            'content': 'Content',
            'excerpt': 'Excerpt',
            'image': 'Image',
            }

        image = forms.ImageField(label='Image', required=True, widget=CustomClearableFileInput)
