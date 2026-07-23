from rest_framework import serializers


class DashboardSerializer(serializers.Serializer):
    books = serializers.IntegerField()
    authors = serializers.IntegerField()
    categories = serializers.IntegerField()
    users = serializers.IntegerField()
    borrowed_books = serializers.IntegerField()
    available_books = serializers.IntegerField()