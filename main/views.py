from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Posts


# Create your views here.

class NewPost(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ["title", "content"]
    template_name = "posts/new_post.html"
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostsView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = "posts/posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Posts.objects.filter(
            user=self.request.user
        )


class AllPostsView(ListView):
    model = Posts
    template_name = "posts/posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Posts.objects.select_related("user").order_by("-created_at")
