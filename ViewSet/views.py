from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from ViewSet.models import Book
from ViewSet.serializers import BookSerializer
from rest_framework import status
from rest_framework import viewsets

# from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.authentication import BasicAuthentication
from rest_framework.throttling import UserRateThrottle

from rest_framework.pagination import PageNumberPagination

class BookViewSet(viewsets.ViewSet):

    def list(self,request):
        book = Book.objects.all()

        # serializer = BookSerializer(book,many=True)
        # return Response(serializer.data)

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(book, request)

        if page is not None:
            serializer = BookSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = BookSerializer(book, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # permission_classes = [BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    def get_permissions(self):
        if self.action == 'retrieve': 
            permission_classes = [IsAuthenticated]
        else:
            permission_classes=[AllowAny]
            # permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    

    def retrieve(self,request,pk=None):
        id = pk
        if id is not None:
            book = Book.objects.get(id=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data)
    
    def create(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        id = pk
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data update'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Partial data update'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        id = pk
        book = Book.objects.get(pk=id)
        book.delete()
        return Response({'message':'Data deleted'})
    