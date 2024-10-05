from django.db import models
from users.models import User
from django.utils import timezone


class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    number = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    pages = models.IntegerField()
    cover = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Loan(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateField(default=timezone.now)
    return_date = models.DateField()

    def __str__(self):
        return f'{self.user} - {self.book}'
