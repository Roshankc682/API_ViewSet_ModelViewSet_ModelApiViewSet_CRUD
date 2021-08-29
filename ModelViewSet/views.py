from ModelViewSet.models import Book
from ModelViewSet.serializers import BookSerializer
from rest_framework import viewsets

class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer