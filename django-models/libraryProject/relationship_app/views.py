from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import permission_required
from .models import Book, Library  # ✅ Explicitly importing Library

# List all books (Function-based view)
def list_books(request):
    books = Book.objects.all()
    try:
        return render(request, 'relationship_app/list_books.html', {'books': books})
    except:
        book_list = "\n".join([f"{book.title} by {book.author.name}" for book in books])
        return HttpResponse(f"<pre>{book_list}</pre>")

# Library detail view (Class-based view)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Secured views for Book model
@permission_required('relationship_app.can_add_book')
def add_book(request):
    return HttpResponse("Add book view (permission required)")

@permission_required('relationship_app.can_change_book')
def edit_book(request):
    return HttpResponse("Edit book view (permission required)")

@permission_required('relationship_app.can_delete_book')
def delete_book(request):
    return HttpResponse("Delete book view (permission required)")