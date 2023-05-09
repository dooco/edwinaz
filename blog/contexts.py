from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.utils import timezone


def post_list_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    template = 'blog/post_list.html'

    return render(request, template, context)
