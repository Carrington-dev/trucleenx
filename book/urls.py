from django.urls import path
from book import views

urlpatterns = [
    path("calendar/", views.book, name="calendar"),
    path("book_second/", views.book_second, name="book_second"),
     path('cities/', views.autocomplete, name='autocomplete'),
     path('slots/', views.autocomplete2, name='autocomplete2'),
     path('done/', views.done, name='done'),
]