from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from main.forms import BookForm
from .models import Book


def home(request):
    return render(request, "home.html", {})


def login_user(request):
    # login user

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "GET":
        return render(request, "login.html", {})

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.success(request, "از نام کاربری یا رمز عبور دیگری استفاده کنید!")
            return redirect("login")

        login(request, user)
        messages.success(request, "به کتابخانه خوش آمدید")
        return redirect("home")


def logout_user(request):
    # if not request.method == "POST":
    #     messages.success(request, "مشکلی در ارتباط با سرور")
    #     return redirect("home")

    logout(request)
    messages.success(request, "با موفقیت خارج شدید")
    return redirect("home")


def books(request):
    if not request.user.is_authenticated:
        messages.success(request, "برای دسترسی باید وارد حساب کاربری خود شوید")
        return redirect("home")

    books = Book.objects.all()

    return render(request, "books.html", {"books": books})


def add_book(request):
    if not request.user.is_authenticated:
        messages.success(request, "برای دسترسی باید وارد حساب کاربری خود شوید")
        return redirect("home")

    if request.method == "GET":
        form = BookForm()
        return render(request, "book/add.html", {"form": form})

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data["name"]
            book_author = form.cleaned_data["author"]

            Book.objects.create(name=book_name, author=book_author)

            messages.success(request, "کتاب با موفقیت ساخته شد")
            return redirect("books")
        return render(request, "book/add.html", {"form": form})


def book(request, pk):
    if not request.user.is_authenticated:
        messages.success(request, "برای دسترسی باید وارد حساب کاربری خود شوید")
        return redirect("login")

    book = Book.objects.get(id=pk)

    if not book:
        messages.success(request, "کتابی با این شماره موجود نیست")
        return render(request, "books.html", {})

    return render(request, "book/book.html", {"book": book})


def update(request, pk):
    if not request.user.is_authenticated:
        messages.success(request, "برای دسترسی باید وارد حساب کاربری خود شوید")
        return redirect("login")

    book = Book.objects.get(id=pk)

    if request.method == "GET":
        form = BookForm(instance=book)
        return render(request, "book/update.html", {"form": form})

    if request.method == "POST":
        form = BookForm(request.POST)

        if not form.is_valid():
            messages.success(request, "مقادیر ورودی را تغییر دهید")
            return render(request, "book/update.html", {"form": form})

        book.name = form.cleaned_data["name"]
        book.author = form.cleaned_data["author"]

        book.save()

        messages.success(request, "کتاب بروزرسانی شد")
        return redirect("books")
