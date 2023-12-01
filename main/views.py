from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


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
