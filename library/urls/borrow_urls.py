from django.urls import path

from library.views.borrow_views import (
    BorrowBookView,
    MyBorrowedBooksView,
    ReturnBookView,
)

urlpatterns = [
    path(
        "",
        BorrowBookView.as_view(),
        name="borrow-book",
    ),

    path(
        "return/<int:pk>/",
        ReturnBookView.as_view(),
        name="return-book",
    ),

    path(
        "my-books/",
        MyBorrowedBooksView.as_view(),
        name="my-books",
    ),
]