from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("books", views.books, name="books"),
    path("addbook", views.add_book, name="addbook"),
    path("book/<int:pk>", views.book, name="book"),
    path("update/<int:pk>", views.update, name="update"),
    path("remove/<int:pk>", views.remove, name="remove"),
    path("clients", views.clients, name="clients"),
    path("addclient", views.addclient, name="addclient"),
]
