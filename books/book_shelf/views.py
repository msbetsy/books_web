from django.shortcuts import render, get_object_or_404
from .models import Book


# Create your views here.

def book_list(request):
    """Create view for all books."""
    books = Book.published.all()
    return render(request, 'book_shelf/book_list.html', {'books': books})


def book_info(request, year, book_id):
    """Create detail view for the book."""
    book = get_object_or_404(Book,
                             status='published',
                             year=year,
                             id=book_id
                             )
    return render(request, 'book_shelf/book_info.html', {'book': book})
