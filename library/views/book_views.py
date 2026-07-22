from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from library.filters import BookFilter
from library.models import Book
from library.permissions import IsStaffOrReadOnly
from library.serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):

    queryset = Book.objects.select_related(
        "author",
        "category",
    )

    serializer_class = BookSerializer

    permission_classes = [
        IsStaffOrReadOnly,
    ]

    filter_backends = [

        DjangoFilterBackend,

        filters.SearchFilter,

        filters.OrderingFilter,

    ]

    filterset_class = BookFilter

    search_fields = [

        "title",

        "isbn",

        "author__name",

        "category__name",

    ]

    ordering_fields = [

        "title",

        "created_at",

        "updated_at",

    ]

    ordering = [
        "title",
    ]


class BookDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Book.objects.select_related(
        "author",
        "category",
    )

    serializer_class = BookSerializer

    permission_classes = [
        IsStaffOrReadOnly,
    ]