from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    
    # Render using template in the app folder for ALX compliance
    try:
        return render(request, 'relationship_app/list_books.html', {'books': books})
    except:
        # Fallback to plain text if template not found
        book_list = "\n".join([f"{book.title} by {book.author.name}" for book in books])
        return HttpResponse(f"<pre>{book_list}</pre>")

# Class-based view to show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ALX requires app folder
    context_object_name = 'library'