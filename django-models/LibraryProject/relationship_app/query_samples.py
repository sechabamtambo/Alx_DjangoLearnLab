import django, os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from relationship_app.models import Author, Library

# 1. All books by a specific author
author = Author.objects.get(name="J.K. Rowling")
print("Books by J.K. Rowling:", [book.title for book in author.books.all()])

# 2. All books in a library
library = Library.objects.get(name="Central Library")
print("Books in Central Library:", [book.title for book in library.books.all()])

# 3. Librarian for a library
print("Librarian of Central Library:", library.librarian.name)
