from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from .forms import BookForm,StudentForm,StudentForm2,BookCoverForm,SignUpForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

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

def booklist1(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/booklist1.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = float(request.POST.get('price'))
        edition = int(request.POST.get('edition'))

        Book.objects.create(
            title=title,
            author=author,
            price=price,
            edition=edition
        )
        return redirect('/books/lab9_part1/booklist1')

    return render(request, 'bookmodule/add_book.html')

def edit_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = float(request.POST.get('price'))
        book.edition = int(request.POST.get('edition'))
        book.save()
        return redirect('/books/lab9_part1/booklist1')

    return render(request, 'bookmodule/edit_book.html', {'book': book})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('/books/lab9_part1/booklist1')


def booklist2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/booklist2.html', {'books': books})

def add_book2(request):
    form = BookForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/books/lab9_part2/booklist2')
    return render(request, 'bookmodule/add_book2.html', {'form': form})

def edit_book2(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=book)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/books/lab9_part2/booklist2')
    return render(request, 'bookmodule/edit_book2.html', {'form': form, 'book': book})

def delete_book2(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
        return redirect('/books/lab9_part2/booklist2')
    return render(request, 'bookmodule/delete_book2.html', {'book': book})

def list_student(request):
    students =Student.objects.all()
    return render(request,'bookmodule/list_student.html',{'students':students})      

def add_student(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('students.list_student')
    return render(request,'bookmodule/add_student.html',{'form':form})



def edit_student(request,bID):
    student = Student.objects.get(id=bID)
    if request.method=='POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid:
            form.save()
            return redirect('students.list_student')
    form = StudentForm(instance=student)
    return render(request,'bookmodule/add_student.html',{'form':form})


def delete_student(request,bID):
    student = Student.objects.get(id=bID)
    student.delete()
    return redirect('students.list_student')

def list_student2(request):
    if request.user.is_authenticated:
        students = Student2.objects.all()
        return render(request,'bookmodule/list_student2.html',{'students':students})  
    else:
        return redirect(register)     

def add_student2(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=StudentForm2(request.POST)
            if form.is_valid:
                form.save()
                return redirect('students.list_student2')
        else:
            form=StudentForm2()
            return render(request,'bookmodule/add_student.html',{'form':form})
    else:
        return redirect(register)    



def edit_student2(request,bID):
    if request.user.is_authenticated:
        student = Student2.objects.get(id=bID)
        if request.method=='POST':
            form = StudentForm2(request.POST,instance=student)
            if form.is_valid:
                form.save()
                return redirect('students.list_student2')
        form = StudentForm2(instance=student)
        return render(request,'bookmodule/add_student.html',{'form':form})
    else:
        return redirect(register)


def delete_student2(request,bID):
    if request.user.is_authenticated:
        student = Student2.objects.get(id=bID)
        student.delete()
        return redirect('students.list_student2')
    else:
        return redirect(register)

def addBookWithCover(request):
    if request.method=='POST':
        form = BookCoverForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            books =BookCover.objects.all()
            return render(request,'bookmodule/listBooksCovers.html',{'books':books})
        else:
            print(form.errors)

    form = BookCoverForm(None)
    return render(request,'bookmodule/addbookcover.html',{'form':form})

def homepage(request):
    return redirect(list_student2)





def register(request):
    form =SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            login(request, user)
            messages.success(request, "You Have Successfully Registered!")
            return redirect(homepage)
        else:
            messages.error(request, form.error_messages)
    return render(request,'bookmodule/register.html',{'form':form})



def logoutuser(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect(register)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect(homepage)
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'bookmodule/login.html')


def lab12task1(request):
    return render(request,'bookmodule/lab12_task1.html')

def lab12task2(request):
    return render(request,'bookmodule/lab12_task2.html')

def lab12task3(request):
    return render(request,'bookmodule/lab12_task3.html')

def lab12task4(request):
    return render(request,'bookmodule/lab12_task4.html')

def lab12task5(request):
    return render(request,'bookmodule/lab12_task5.html')