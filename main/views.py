from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Posts


# Create your views here.
# creating new posts
class NewPost(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ["title", "content"]
    template_name = "posts/new_post.html"
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Displays user's posts only.
class PostsView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = "posts/posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Posts.objects.filter(
            user=self.request.user
        )

# Explores all other users posts.
class AllPostsView(ListView):
    model = Posts
    template_name = "posts/explore.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Posts.objects.select_related("user").order_by("-created_at")


# Deleting posts
class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Posts
    template_name = "posts/post_confirm_delete.html"
    success_url = reverse_lazy("posts")

    def get_queryset(self):
        return Posts.objects.filter(
            user=self.request.user
        )


# Editing Posts
class EditPostView(LoginRequiredMixin, UpdateView):
    model = Posts
    fields = ["title", "content"]
    template_name = "posts/edit_post.html"
    success_url = reverse_lazy("posts")

    def get_queryset(self):
        return Posts.objects.filter(
            user=self.request.user
        )
