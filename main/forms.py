from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    name = forms.CharField(label="نام کتاب", max_length=255, min_length=3)
    author = forms.CharField(label="نام نویسنده", max_length=255, min_length=3)

    class Meta:
        model = Book
        fields = ["name", "author"]
