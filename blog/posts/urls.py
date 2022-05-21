from django.urls import URLPattern, path

from .views import PostListView, PostDetailView

urlpatterns = [
    path('/', PostListView.as_view(), name = 'post-list'),
    path('/<slug:slug>', PostDetailView.as_view(), name = 'post-detail')
]