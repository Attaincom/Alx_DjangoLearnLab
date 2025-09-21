from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# A ViewSet automatically provides list, create, retrieve, update, and delete actions
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
