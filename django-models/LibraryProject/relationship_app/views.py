from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from .models import Library
from .models import Book, Author
from django.contrib.auth.decorators import login_required, user_passes_test

# -------------------------------
# BOOK & LIBRARY VIEWS
# -------------------------------
def list_books(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {
        'books': books,
        'library': library
    })


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# -------------------------------
# AUTH VIEWS
# -------------------------------
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


# -------------------------------
# ROLE CHECK FUNCTIONS
# -------------------------------
def is_Admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


def is_Librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


def is_Member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# -------------------------------
# ROLE-BASED VIEWS
# -------------------------------
@login_required
@user_passes_test(is_Admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@login_required
@user_passes_test(is_Librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@login_required
@user_passes_test(is_Member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
