from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Library
from .models import Book, Author

def list_books(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    books = Book.objects.filter(library=library)  # show only books from that library
    return render(request, 'relationship_app/list_books.html', {
        'books': books,
        'library': library
    })


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # corrected path
    context_object_name = 'library'
