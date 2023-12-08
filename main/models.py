from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    bookLandedNumber = models.IntegerField(
        validators=[MaxValueValidator(2), MinValueValidator(0)]
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    isRented = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Landing(models.Model):
    date = models.DateField()
    books = models.ManyToManyField(Book, related_name="landings")
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name="client")

    def __str__(self):
        return ""
