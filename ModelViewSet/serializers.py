from rest_framework import serializers
from ModelViewSet.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title','description','price']
        