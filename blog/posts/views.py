from .models import Post

from django.views.generic import ListView, DetailView


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.published()


class PostDetailView(DetailView):
    model = Post
