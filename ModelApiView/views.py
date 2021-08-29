from ModelApiView.models import Book
from ModelApiView.serializers import BookSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny

from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveAPIView, UpdateAPIView , DestroyAPIView

from rest_framework.generics import (
                                     ListCreateAPIView , 
                                     RetrieveUpdateAPIView,
                                     RetrieveDestroyAPIView , 
                                     RetrieveUpdateDestroyAPIView
                                     )

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # use this to authenticate for one class but this is tedious 
    # so import it in settings 
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    # or for any user to allow
    # permission_classes=[AllowAny]


class BookCreate(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieve(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdate(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDelete(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



# listed and create in one class
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve and Update in one class
class BookRetreiveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveDestroyAPIview(RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyAPIview(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



