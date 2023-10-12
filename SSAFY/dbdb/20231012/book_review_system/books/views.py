from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request, 'books/index.html', context)


def detail(request, pk):
    book = Book.objects.get(pk=pk)
    form = ReviewForm()
    context = {
        'book':book,
        'form':form,
    }
    return render(request, 'books/detail.html', context)


def create_review(request, pk):
    book = Book.objects.get(pk=pk)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.book = book
        form.save()
        return redirect('books:detail', pk)
    context = {
        'form':form,
    }
    return render(request, 'books/detail.html', context)


def delete_review(request, book_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('books:detail', book_pk)