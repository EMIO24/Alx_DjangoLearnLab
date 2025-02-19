from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('books/', book_list, name = 'book-list')
]