from django.urls import path
from .views import (
    CreatePost, PostDetailView, EditPost, DeletePost, PostsListView, RandomPostsView
)
from . import views


urlpatterns = [
    path('', PostsListView.as_view(), name='posts'),
    path('photo/', views.photo_carousel, name='photo_carousel'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('add/', CreatePost.as_view(), name='add_post'),
    path('edit/<slug:pk>/', EditPost.as_view(), name='edit_post'),
    path('delete/<slug:pk>/', DeletePost.as_view(), name='delete_post'),
    path('random/', RandomPostsView.as_view(), name='random_posts'),

]
