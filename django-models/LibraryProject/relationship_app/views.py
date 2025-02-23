from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
  
class LibraryDetailView(DetailView):
    """
    A class-based view to display details of a specific library and list all books in that library.
    """
    model = Library  # The model to use for the view
    template_name = 'relationship_app/library_detail.html'  # The template to render
    context_object_name = 'library'  # The name of the context variable in the template

    def get_context_data(self, **kwargs):
        """
        Add additional context data to the template.
        """
        # Call the base implementation first to get the default context
        context = super().get_context_data(**kwargs)

        # Add the list of books in the library to the context
        context['books'] = self.object.books.all()  # Access books using the related_name 'books'
        return context
# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")  # Redirect to login page after signup
