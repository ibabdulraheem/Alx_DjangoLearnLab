from django.shortcuts import render
from .models import Book
from .models import Library
from relationship_app.models import Book
from relationship_app.models import Library
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy,path
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login
# Create your views here.


# LibraryProject/relationship_app/views.py doesn't contain: ["relationship_app/library_detail.html"]
""" creating view for a book model """
def list_books (request):
  books = Book.objects.all() 
  return render(request, 'relationship_app/list_books.html')

class BookListView(ListView):
  model = Library
  books = Library.objects.get(name = 'library_name')
  for book in books:
    print(book)
  template_name = 'library_detail.html'
  success_url = reverse_lazy('book')

""" User registration view""" 
class SignUpView(CreateView):
  form_class = UserCreationForm
  template_name = 'register.html'
  success_url = reverse_lazy('login')

""" User Login View"""
class UserLoginView(LoginView):
    template_name = 'login.html' 
    redirect_authenticated_user = True 

    def get_success_url(self):
        return reverse_lazy('dashboard')

""" Use Logout View"""
class UserLogoutView(LogoutView):
    template_name = 'logout.html'

    def dispatch(self, request, *args, **kwargs):
        return reverse_lazy('home_page')