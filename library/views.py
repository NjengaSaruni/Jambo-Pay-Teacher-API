from rest_framework import generics

from library.models import Book
from library.serializers import BookSerializer, BookListSerializer


class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookListSerializer
        return BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookListSerializer
        return BookSerializer
