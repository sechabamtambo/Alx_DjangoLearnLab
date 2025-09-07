from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('books/add_book/', views.add_book, name='add_book'),
    path('books/edit_book/', views.edit_book, name='edit_book'),
    path('books/delete_book/', views.delete_book, name='delete_book'),
]