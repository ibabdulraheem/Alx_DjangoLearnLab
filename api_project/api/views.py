
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser
from .models import Book

class BookViewSetIsAuthenticated(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookViewSetIsAdminUser(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]



    

# Create your views here.

# class BookList(generics.ListAPIView):
#   queryset = Book.objects.all()
#   serializer_class = BookSerializer

# ["BookViewSet"]
# class BookViewSet(viewsets.ModelViewSet):
#   queryset = Book.objects.all()
#   serializer_class = BookSerializer


  
