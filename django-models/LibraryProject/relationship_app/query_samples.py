import django, os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from relationship_app.models import Author, Library

author = Author.objects.get(name="J.K. Rowling")
print("Books by J.K. Rowling:", [book.title for book in author.books.all()])

library = Library.objects.get(name="Central Library")
print("Books in Central Library:", [book.title for book in library.books.all()])

print("Librarian of Central Library:", library.librarian.name)
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Library

author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)
print("Books by J.K. Rowling:", [book.title for book in author.books.all()])

library_name = "Central Library"
library = Library.objects.get(name=library_name)  # <-- this line must be exactly like this
print("Books in Central Library:", [book.title for book in library.books.all()])

print("Librarian of Central Library:", library.librarian.name)