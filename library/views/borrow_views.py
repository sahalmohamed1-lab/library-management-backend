from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from library.models import Book, BorrowRecord
from library.serializers import BorrowRecordSerializer

class BorrowBookView(APIView):
    def post(self, request):
        book_id = request.data.get("book")

        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response(
                {"error": "Book not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        if not book.available:
            return Response(
                {"error": "Book is already borrowed."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        borrow = BorrowRecord.objects.create(
            user=request.user,
            book=book,
        )

        book.available = False
        book.save()

        serializer = BorrowRecordSerializer(borrow)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ReturnBookView(APIView):
    def post(self, request, pk):
        try:
            borrow = BorrowRecord.objects.get(
                pk=pk,
                user=request.user,
                returned=False,
            )
        except BorrowRecord.DoesNotExist:
            return Response(
                {"error": "Borrow record not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        borrow.returned = True
        borrow.return_date = timezone.now()
        borrow.save()

        book = borrow.book
        book.available = True
        book.save()

        return Response(
            {"message": "Book returned successfully."}
        )
    
class MyBorrowedBooksView(generics.ListAPIView):
    serializer_class = BorrowRecordSerializer

    def get_queryset(self):
        return BorrowRecord.objects.filter(
            user=self.request.user,
            returned=False,
        ).select_related("book", "user")