from django.contrib import admin
from ModelApiView.models import Book


@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display = ['id','title','description','price']