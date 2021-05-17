from django.shortcuts import render, redirect
from . models import*

# Create your views here.

def index(request):
    return render(request, 'books.html',{"books": Book.objects.all()})

def authors(request):
    return render(request, 'authors.html',{"authors":Author.objects.all()})

def create_book(request):
    Book.objects.create(title=request.POST['title'],description=request.POST['description'])
    return redirect('/books')

def create_author(request):
    Author.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],notes=request.POST['notes'])
    return redirect('/authors')

def show_book(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        "book": book,
        #"authors": Author.objects.exclude(books__id=book_id)
    }
    return render(request, 'book.html',context)

def show_author(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        "author": author,
    }
    return render(request, 'author.html',context)