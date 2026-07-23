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
        fields = (
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
        )
        read_only_fields = (
            "id",
            "user",
            "username",
            "book_title",
            "borrow_date",
            "return_date",
            "returned",
            "created_at",
            "updated_at",
        )

    def validate(self, attrs):
        request = self.context["request"]
        book = attrs["book"]
        if not book.available:
            raise serializers.ValidationError(
                {
                    "book": "This book is currently unavailable."
                }
            )
        already_borrowed = BorrowRecord.objects.filter(
            user=request.user,
            book=book,
            returned=False,
        ).exists()
        if already_borrowed:
            raise serializers.ValidationError(
                {
                    "book": "You have already borrowed this book."
                }
            )
        return attrs

    def create(self, validated_data):
        request = self.context["request"]
        borrow = BorrowRecord.objects.create(
            user=request.user,
            book=validated_data["book"],
        )
        borrow.book.available = False
        borrow.book.save()
        return borrow