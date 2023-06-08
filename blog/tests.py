from django.test import TestCase, Client
import unittest
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post


class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.post = Post.objects.create(
            user=self.user,
            title='Test Article',
            content='This is a test article content',
            excerpt='Test excerpt',
            image=None,
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Article')
        self.assertEqual(self.post.content, 'This is a test article content')
        self.assertEqual(self.post.excerpt, 'Test excerpt')
        self.assertEqual(self.post.image, None)
        self.assertIsNotNone(self.post.date_added)
        self.assertEqual(str(self.post), 'Test Article')

    def test_post_ordering(self):
        post2 = Post.objects.create(
            user=self.user,
            title='Second Article',
            content='This is the second article content',
            excerpt='Second article excerpt',
            image=None,
        )
        posts = Post.objects.all()
        self.assertEqual(posts[0], self.post)
        self.assertEqual(posts[1], post2)

    if __name__ == '__main__':
        unittest.main()


class BlogAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.post = Post.objects.create(
            title='Test Article',
            content='This is a test article',
            user=self.user
        )

    def test_posts_list_view(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_detail_view(self):
        response = self.client.get(
            reverse(
                'post_detail', kwargs={
                    'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_create_post_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('add_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/add_post.html')

    def test_edit_post_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(
            reverse(
                'edit_post', kwargs={
                    'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit_post.html')

    def test_delete_post_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(
            reverse(
                'delete_post', kwargs={
                    'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_confirm_delete.html')
