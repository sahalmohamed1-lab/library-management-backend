from django.utils import timezone
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from library.models import BorrowRecord
from library.serializers import BorrowRecordSerializer

class BorrowBookView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = BorrowRecordSerializer(
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        borrow = serializer.save()
        return Response(
            BorrowRecordSerializer(borrow).data,
            status=status.HTTP_201_CREATED,
        )

class ReturnBookView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        try:
            borrow = BorrowRecord.objects.get(
                pk=pk,
                user=request.user,
                returned=False,
            )
        except BorrowRecord.DoesNotExist:
            return Response(
                {
                    "error": "Borrow record not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        borrow.returned = True
        borrow.return_date = timezone.now()
        borrow.save()
        book = borrow.book
        book.available = True
        book.save()
        return Response(
            {
                "message": "Book returned successfully."
            }
        )

class MyBorrowedBooksView(generics.ListAPIView):
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return BorrowRecord.objects.filter(
            user=self.request.user,
            returned=False,
        ).select_related(
            "user",
            "book",
        )