from django import forms

from .models import Book, Loan


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('number', 'title', 'release_date',
                  'author', 'description', 'pages', 'cover')


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ('book', 'user', 'borrow_date', 'return_date')
