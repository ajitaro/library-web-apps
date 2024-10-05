
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.utils import timezone
from datetime import timedelta
import requests
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Book, Loan
from .forms import BookForm, LoanForm


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:dashboard')
        return super().get(request, *args, **kwargs)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_staff:
            context['is_admin'] = True
            loan = Loan.objects.all()
            context['loans'] = loan
        else:
            loans = Loan.objects.filter(user=user)
            context['loans'] = loans

        return context


class BookListView(ListView):
    template_name = 'core/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'


class BookCreateView(StaffRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    success_url = '/books'


class BookUpdateView(StaffRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    success_url = '/books'


class BookDeleteView(StaffRequiredMixin, DeleteView):
    model = Book
    success_url = '/books'


class LoanListView(LoginRequiredMixin, ListView):
    model = Loan
    context_object_name = 'dashboard'

    def get_queryset(self):
        return Loan.objects.filter(user=self.request.user)


class LoanDetailView(LoginRequiredMixin, DetailView):
    model = Loan
    context_object_name = 'loan'

    def get_queryset(self):
        return Loan.objects.filter(user=self.request.user)


class LoanCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('book_id')
        book = get_object_or_404(Book, number=book_id)
        existing_loan = Loan.objects.filter(user=request.user).first()

        if existing_loan:
            messages.warning(request,
                             (f'Kamu sedang meminjam buku {existing_loan.book.title}.'
                              f'\n Kamu harus mengembalikan buku itu sebelum meminjam buku baru.'))
            return redirect('core:dashboard')

        borrow_date = timezone.now().date()
        return_date = borrow_date + timedelta(days=14)

        Loan.objects.create(user=request.user, book=book,
                            borrow_date=borrow_date, return_date=return_date)

        messages.success(
            request, f"Kamu berhasil meminjam buku '{book.title}'.")
        return redirect('core:dashboard')


class LoanUpdateView(LoginRequiredMixin, UpdateView):
    model = Loan
    form_class = LoanForm
    success_url = '/dashboard'

    def get_queryset(self):
        return Loan.objects.filter(user=self.request.user)


class LoanDeleteView(LoginRequiredMixin, DeleteView):
    model = Loan
    success_url = '/dashboard'

    def get_queryset(self):
        return Loan.objects.filter(user=self.request.user)


class ImportBooksView(StaffRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        books = self.get_books_from_api()
        count = 0
        for book_data in books:
            book, created = Book.objects.get_or_create(
                number=book_data.get('number'),
                title=book_data.get('title'),
                release_date=book_data.get('releaseDate'),
                description=book_data.get('description'),
                pages=book_data.get('pages'),
                cover=book_data.get('cover')
            )
            if created:
                count += 1
        messages.success(request, f'{count} buku berhasil di-import.')
        return redirect('core:dashboard')

    def get_books_from_api(self):
        try:
            response = requests.get(
                'https://potterapi-fedeperin.vercel.app/en/books')
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            messages.error(self.request, f"Error fetching books: {e}")
            return []
