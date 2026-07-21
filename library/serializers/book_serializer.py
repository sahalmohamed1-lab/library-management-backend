import re

from rest_framework import serializers

from library.models import Book


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(
        source="author.name",
        read_only=True,
    )

    category_name = serializers.CharField(
        source="category.name",
        read_only=True,
    )

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "isbn",
            "author",
            "author_name",
            "category",
            "category_name",
            "available",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
            "author_name",
            "category_name",
        )

    def validate_title(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Title cannot be empty."
            )

        return value

    def validate_isbn(self, value):
        value = value.replace("-", "").strip()

        if not re.fullmatch(r"\d{13}", value):
            raise serializers.ValidationError(
                "ISBN must contain exactly 13 digits."
            )

        queryset = Book.objects.filter(isbn=value)

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                "ISBN already exists."
            )

        return value