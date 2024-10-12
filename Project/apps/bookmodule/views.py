from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    return render(request, "bookmodule/index.html")



def list_books(request):

    return render(request, 'bookmodule/list_books.html')



def viewbook(request):

    return render(request, 'bookmodule/one_book.html')



def aboutus(request):

    return render(request, 'bookmodule/aboutus.html')