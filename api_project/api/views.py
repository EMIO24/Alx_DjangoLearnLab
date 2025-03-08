# Create your views here.
from rest_framework import generics
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # This gets all the books from the database
    serializer_class = BookSerializer  # This tells Django how to convert the book data to JSON and back