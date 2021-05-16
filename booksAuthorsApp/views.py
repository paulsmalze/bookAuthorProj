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
    Book.objects.create(title=request.POST['first_name'],description=request.POST['last_name'],notes=request.POST['notes'])
    return redirect('/authors')