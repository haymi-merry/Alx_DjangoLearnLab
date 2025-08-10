from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from .models import Library
from .models import Book, Author

def list_books(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {
        'books': books
    })


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # corrected path
    context_object_name = 'library'

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html' 

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
