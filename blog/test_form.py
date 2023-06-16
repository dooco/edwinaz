from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from .forms import PostForm
import os
from django.conf import settings


class PostFormTest(TestCase):
    """ Unit tests for blog forms """
    def test_post_form_valid(self):
        # Create a valid form data dictionary
        form_data = {
            'title': 'Test Title',
            'content': 'Test Content',
            'excerpt': 'Test Excerpt',
        }

        # Specify the file path relative to the 'media' folder
        file_path = 'images/bed-gold.jpg'

        # Construct the absolute file path
        absolute_file_path = os.path.join('media', file_path)

        # Open and read the file content
        with open(absolute_file_path, 'rb') as file:
            file_content = file.read()

        # Create a SimpleUploadedFile instance with the file content and
        # content type
        image_file = SimpleUploadedFile(
            name='bed-gold.jpg',
            content=file_content,
            content_type='image/jpeg')

        # Create a form instance with the form data and image file
        form = PostForm(data=form_data, files={'image': image_file})

        if not form.is_valid():
            print(form.errors)

        self.assertTrue(form.is_valid())

    def test_post_form_invalid(self):
        # Create an invalid form data dictionary with missing required fields
        form_data = {
            'title': '',  # Empty title (required field)
            'content': 'Test Content',
            'excerpt': 'Test Excerpt',
        }

        # Create a form instance with the invalid form data
        form = PostForm(data=form_data)

        # Check if the form is invalid
        self.assertFalse(form.is_valid())
        # Check if 'title' field has an error
        self.assertIn('title', form.errors.keys())

        # Check for specific error messages
        self.assertEqual(form.errors['title'], ['This field is required.'])
