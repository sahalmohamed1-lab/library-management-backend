from rest_framework import serializers

from library.models import BorrowRecord


class BorrowRecordSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        source="user.username",
        read_only=True,
    )

    book_title = serializers.CharField(
        source="book.title",
        read_only=True,
    )

    class Meta:
        model = BorrowRecord
        fields = [
            "id",
            "user",
            "username",
            "book",
            "book_title",
            "borrow_date",
            "return_date",
            "returned",
            "created_at",
            "updated_at",
        ]

        read_only_fields = (
            "id",
            "user",
            "borrow_date",
            "return_date",
            "returned",
            "created_at",
            "updated_at",
            "username",
            "book_title",
        )