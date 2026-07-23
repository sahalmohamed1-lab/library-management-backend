import django_filters

from library.models import Book

class BookFilter(django_filters.FilterSet):
    available = django_filters.BooleanFilter()
    category = django_filters.NumberFilter(
        field_name="category__id"
    )
    author = django_filters.NumberFilter(
        field_name="author__id"
    )
    class Meta:
        model = Book
        fields = [
            "available",
            "category",
            "author",
        ]