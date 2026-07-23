from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from library.models import Author, Book, BorrowRecord, Category
from library.serializers.dashboard_serializer import DashboardSerializer


class DashboardAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        data = {
            "books": Book.objects.count(),
            "authors": Author.objects.count(),
            "categories": Category.objects.count(),
            "users": User.objects.count(),
            "borrowed_books": BorrowRecord.objects.filter(
                returned=False
            ).count(),
            "available_books": Book.objects.filter(
                available=True
            ).count(),
        }

        serializer = DashboardSerializer(data)

        return Response(serializer.data)