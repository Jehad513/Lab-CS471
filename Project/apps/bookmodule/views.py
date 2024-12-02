from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Student, Address
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min

# Create your views here.

def index(request):

    return render(request, "bookmodule/index.html")


def list_books(request):

    return render(request, 'bookmodule/list_books.html')


def viewbook(request):

    return render(request, 'bookmodule/one_book.html')


def aboutus(request):

    return render(request, 'bookmodule/aboutus.html')


def html5(request):

    return render(request, 'bookmodule/html5.html')


def links(request):

    return render(request, 'bookmodule/links.html')



def viewFormat(request):

    return render(request, 'bookmodule/formating.html')


def viewListing(request):

    return render(request, 'bookmodule/listing.html')


def viewTable(request):

    return render(request, 'bookmodule/tables.html')


def viewSearch(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
 # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})

    return render(request,'bookmodule/search.html')
    


def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]


def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1: 
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def book_list_task1(request):
    books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'bookmodule/book_list_task1.html', {'books': books})

def book_list_task2(request):
    books = Book.objects.filter(Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/book_list_task2.html', {'books': books})

def book_list_task3(request):
    books = Book.objects.filter(~Q(edition__gt=2) & ~Q(title__icontains='qu') & ~Q(author__icontains='qu'))
    return render(request, 'bookmodule/book_list_task3.html', {'books': books})

def book_list_task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/book_list_task4.html', {'books': books})

def book_list_task5(request):
    book_stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/book_list_task5.html', {'book_stats': book_stats})

def students_per_city(request):
    students_count = Address.objects.annotate(student_count=Count('student')).values('city', 'student_count')
    return render(request, 'bookmodule/students_per_city.html', {'students_count': students_count})