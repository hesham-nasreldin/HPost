from django.urls import path
from . import views


urlpatterns = [
    path("posts", views.PostsView.as_view(), name="posts"),
    path("posts/new-post", views.NewPost.as_view(), name="new-post"),
    path("all-posts", views.AllPostsView.as_view(), name="all-posts"),
    path("delete/<int:pk>", views.DeletePostView.as_view(), name="delete-post")
]
