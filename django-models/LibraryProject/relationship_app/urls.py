from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth import views as auth_views
from .views import register
from . import views




urlpatterns = [
    path("register/", views.register, name="register"),  # New signup URL
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('books/', list_books, name = 'book-list'),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),  # Login
    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),  # Logout
]
