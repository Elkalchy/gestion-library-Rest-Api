# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/books/', views.index, name='index_api'),  # Get all books
    path('api/books/add/', views.ajouter, name='ajouter_api'),  # Add a new book
    path('api/books/<int:book_id>/modify/', views.modif, name='modif_api'),  # Modify book
    path('api/books/<int:book_id>/details/', views.mod_details, name='mod_details_api'),  # Modify book details
    path('api/books/<int:book_id>/delete/', views.supp, name='supp_api'),  # Delete a book
    path('api/books/<int:book_id>/filter/', views.filter_index, name='filter_api'),  # Get id book
    path('api/books/search/', views.rech, name='rech_api'),  # Search books

    #Frontend pages
    path('', views.render_index, name='index'),
    path('add_book.html', views.add_book_page, name='add_book'),
    path('edit_book.html', views.edit_book_page, name='edit_book'),
]
