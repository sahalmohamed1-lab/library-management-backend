from django.conf import settings
from django.db import models

from .book import Book
from .common import TimeStampedModel


class BorrowRecord(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="borrow_records",
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="borrow_records",
    )

    borrow_date = models.DateTimeField(auto_now_add=True)

    return_date = models.DateTimeField(
        null=True,
        blank=True,
    )

    returned = models.BooleanField(default=False)

    class Meta:
        ordering = ["-borrow_date"]

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"