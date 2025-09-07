import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Create authors
author1 = Author.objects.create(name="J.K. Rowling")
author2 = Author.objects.create(name="George Orwell")

# Create books
book1 = Book.objects.create(title="Harry Potter 1", author=author1)
book2 = Book.objects.create(title="Harry Potter 2", author=author1)
book3 = Book.objects.create(title="1984", author=author2)

# Create libraries
library1 = Library.objects.create(name="Central Library")
library2 = Library.objects.create(name="Community Library")

# Add books to libraries
library1.books.add(book1, book3)
library2.books.add(book2)

# Create librarians
Librarian.objects.create(name="Alice", library=library1)
Librarian.objects.create(name="Bob", library=library2)