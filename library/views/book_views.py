from rest_framework import generics

from library.models import Book
from library.serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.select_related(
        "author",
        "category",
    )
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.select_related(
        "author",
        "category",
    )
    serializer_class = BookSerializer