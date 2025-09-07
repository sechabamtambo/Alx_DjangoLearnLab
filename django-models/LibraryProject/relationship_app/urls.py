from django.urls import path
from . import views

urlpatterns = [
    # Book and Library views
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Book permission-based views
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/', views.edit_book, name='edit_book'),
    path('books/delete/', views.delete_book, name='delete_book'),
]