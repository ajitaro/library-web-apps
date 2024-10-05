from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/',
         views.BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/',
         views.BookDeleteView.as_view(), name='book-delete'),
    path('loans/', views.LoanListView.as_view(), name='loan-list'),
    path('loans/<int:pk>/', views.LoanDetailView.as_view(), name='loan-detail'),
    path('loans/<int:book_id>/create/',
         views.LoanCreateView.as_view(), name='loan-create'),
    path('loans/<int:pk>/update/',
         views.LoanUpdateView.as_view(), name='loan-update'),
    path('loans/<int:pk>/delete/',
         views.LoanDeleteView.as_view(), name='loan-delete'),
    path('import-books/', views.ImportBooksView.as_view(), name='import-books'),

]
