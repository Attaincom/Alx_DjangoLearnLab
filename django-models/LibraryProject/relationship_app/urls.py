from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import register_view  # keep your function-based register
from django.contrib.auth.views import LoginView, LogoutView  # built-in class-based views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register_view, name='register'),  # function-based register
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
