from django.urls import path
from library.views.author_views import (
    AuthorDetailView,
    AuthorListCreateView,
)

urlpatterns = [
    path("", AuthorListCreateView.as_view(), name="author-list"),
    path("<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
]