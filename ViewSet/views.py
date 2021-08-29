from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from ViewSet.models import Book
from ViewSet.serializers import BookSerializer
from rest_framework import status
from rest_framework import viewsets

class BookViewSet(viewsets.ViewSet):
    def list(self,request):
        book = Book.objects.all()
        serializer = BookSerializer(book,many=True)
        return Response(serializer.data)
    
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