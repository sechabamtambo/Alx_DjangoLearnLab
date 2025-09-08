from .models import Author, Book, Library


def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()


def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian