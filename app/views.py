# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render



# Index View (Get All Books)
@api_view(['GET'])
def index(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# Add Book (POST request)
@api_view(['POST'])
def ajouter(request):
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update Book (PUT request)
@api_view(['PUT'])
def modif(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update Book Details (PUT request)
@api_view(['PUT'])
def mod_details(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Book (DELETE request)
@api_view(['DELETE'])
def supp(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Book.DoesNotExist:
        return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

# Search Books (POST request with search query)
@api_view(['POST'])
def rech(request):
    recherche = request.data.get('rech', None)
    if recherche:
        books = Book.objects.filter(Q(title__icontains=recherche) | Q(auteur__icontains=recherche))
    else:
        books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def filter_index(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    serializer = BookSerializer(book)
    return Response(serializer.data)

# Rendre la page index.html
def render_index(request):
    return render(request, 'index.html')

def add_book_page(request):
    return render(request, 'add_book.html')

def edit_book_page(request):
    return render(request, 'edit_book.html')