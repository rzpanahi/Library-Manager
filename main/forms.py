from django import forms
from .models import Book, Client


class BookForm(forms.ModelForm):
    name = forms.CharField(label="نام کتاب", max_length=255, min_length=3)
    author = forms.CharField(label="نام نویسنده", max_length=255, min_length=3)

    class Meta:
        model = Book
        fields = ["name", "author"]


class ClientForm(forms.ModelForm):
    name = forms.CharField(label="نام کامل", max_length=255, min_length=3)
    email = forms.EmailField(label="ایمیل")

    class Meta:
        model = Client
        fields = ["name", "email"]
