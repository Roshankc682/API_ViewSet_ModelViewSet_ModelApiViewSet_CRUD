from rest_framework import serializers
from ModelViewSet.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','description','price']
        