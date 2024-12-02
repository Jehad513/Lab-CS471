from . import views
from django.urls import path , include

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('viewbook/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/', views.html5, name="books.html5"),
    path('html5/links/', views.links, name="books.html5.links"),
    path('html5/text/formatting', views.viewFormat, name="books.format"),
    path('html5/listing', views.viewListing, name="books.listing"),
    path('html5/tables',views.viewTable, name="books.tables"),
    path('search/',views.viewSearch,name='books.search'),
    path('simple/query',views.simple_query,name='books.simple_query'),
    path('complex/query',views.complex_query,name='books.complex_query'),
    path('lab8/task1', views.book_list_task1, name='book_list_task1'),
    path('lab8/task2', views.book_list_task2, name='book_list_task2'),
    path('lab8/task3', views.book_list_task3, name='book_list_task3'),
    path('lab8/task4', views.book_list_task4, name='book_list_task4'),
    path('lab8/task5', views.book_list_task5, name='book_list_task5'),
    path('students/lab8/task7', views.students_per_city, name='students_per_city'),
    path('lab9_part1/booklist1', views.booklist1, name='booklist1'),
    path('lab9_part1/addbook', views.add_book, name='add_book'),
    path('lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
    path('lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),
    path('lab9_part2/booklist2/', views.booklist2, name='booklist2'),
    path('lab9_part2/addbook2/', views.add_book2, name='add_book2'),
    path('lab9_part2/editbook2/<int:id>/', views.edit_book2, name='edit_book2'),
    path('lab9_part2/deletebook2/<int:id>/', views.delete_book2, name='delete_book2')
]
