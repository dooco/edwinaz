from django.urls import path
from .views import (
    CreatePost, PostDetailView, EditPost, DeletePost, PostsListView
)
from . import views


urlpatterns = [
    path('', PostsListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('add/', CreatePost.as_view(), name='add_post'),
    path('edit/<slug:pk>/', EditPost.as_view(), name='edit_post'),
    path('delete/<slug:pk>/', DeletePost.as_view(), name='delete_post'),
]
