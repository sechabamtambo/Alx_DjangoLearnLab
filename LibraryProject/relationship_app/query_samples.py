import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings') 
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

author1, _ = Author.objects.get_or_create(name="J.K. Rowling")
book1, _ = Book.objects.get_or_create(title="Harry Potter and the Sorcerer's Stone", author=author1)
book2, _ = Book.objects.get_or_create(title="Harry Potter and the Chamber of Secrets", author=author1)

library1, _ = Library.objects.get_or_create(name="Central Library")
library1.books.add(book1, book2)

librarian1, _ = Librarian.objects.get_or_create(name="Alice", library=library1)

books_by_author = Book.objects.filter(author=author1)
print(f"\nBooks by {author1.name}:")
for book in books_by_author:
    print("-", book.title)

books_in_library = library1.books.all()
print(f"\nBooks in {library1.name}:")
for book in books_in_library:
    print("-", book.title)
    
print(f"\nLibrarian of {library1.name}: {library1.librarian.name}")