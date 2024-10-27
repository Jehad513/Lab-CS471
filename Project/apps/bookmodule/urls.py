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
    path('complex/query',views.complex_query,name='books.complex_query')
]
