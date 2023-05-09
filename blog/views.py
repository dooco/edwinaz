from django.shortcuts import render
from django.views.generic import (
 DetailView, CreateView, UpdateView, DeleteView, ListView
)

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)


from .models import Post
from .forms import PostForm


class PostsListView(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        return context


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
    success_url = "/"

    def test_func(self):
        return self.request.user == self.get_object().user


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ A view to delete an article """
    model = Post
    success_url = "/"

    def test_func(self):
        return self.request.user == self.get_object().user


def photo_carousel(request):
    print('photo_carousel View')
    queryset = Post.objects.all()
    context = {
        'photos': queryset,
    }
    return render(request, 'blog/photo_carousel.html', context)