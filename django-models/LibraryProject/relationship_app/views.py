from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import DetailView
from .models import Library
# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    
    # Optional: render HTML template
    try:
        return render(request, 'list_books.html', {'books': books})
    except:
        # fallback to plain text
        book_list = "\n".join([f"{book.title} by {book.author.name}" for book in books])
        return HttpResponse(f"<pre>{book_list}</pre>")
    
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'