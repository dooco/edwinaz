from django.shortcuts import render
from django.contrib import messages
from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView, ListView
)

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from random import sample
from django.views import View
from .models import Post
from .forms import PostForm


class PostsListView(ListView):
    """ View to list articles """
    model = Post


class PostDetailView(DetailView):
    """ View to view an article details"""
    model = Post

    template_name = 'blog/post_detail.html'


class CreatePost(LoginRequiredMixin, CreateView):
    """ View to create an article """
    template_name = 'blog/add_post.html'
    model = Post
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePost, self).form_valid(form)


class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ View to edit an article """
    template_name = 'blog/edit_post.html'
    model = Post
    form_class = PostForm
    success_url = "/blog/"

    def test_func(self):
        return self.request.user == self.get_object().user


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ A view to delete an article """
    model = Post
    success_url = "/blog/"

    def test_func(self):
        return self.request.user == self.get_object().user
