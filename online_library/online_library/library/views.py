from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})
    
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('home')

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Book, Review

def home(request):
    books = Book.objects.all()
    categories = Book.objects.values_list('category', flat=True).distinct()

    query = request.GET.get('q')
    category_filter = request.GET.get('category')

    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query)
    if category_filter:
        books = books.filter(category=category_filter)

    # ✅ THIS PART IS THE IMPORTANT FIX
    return render(request, 'home.html', {
        'books': books,
        'categories': categories,
    })
    
from django.db.models import Avg

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews.all()
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0

    context = {
        'book': book,
        'reviews': reviews,
        'avg_rating': round(avg_rating, 1),  # round to 1 decimal
    }
    return render(request, "book_detail.html", context)

@login_required
def add_review(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        text = request.POST.get("text")
        rating = int(request.POST.get("rating", 0))
        rating = max(1, min(rating, 5))  # Ensure rating is between 1 and 5

        if text:
            Review.objects.create(
                book=book,
                user=request.user,
                text=text,
                rating=rating
            )
            messages.success(request, "Review added successfully!")
            
        return redirect("book_detail", pk=book.pk)

    return render(request, "add_review.html", {"book": book})