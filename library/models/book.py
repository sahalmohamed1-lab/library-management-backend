from django.db import models
from .author import Author
from .category import Category
from .common import TimeStampedModel

class Book(TimeStampedModel):
    title = models.CharField(max_length=200)
    isbn = models.CharField(
        max_length=13,
        unique=True,
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="books",
    )
    available = models.BooleanField(default=True)
    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title