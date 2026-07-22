from django.contrib import admin

from library.models import (
    Author,
    Book,
    BorrowRecord,
    Category,
)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "category",
        "available",
    )
    list_filter = ("category", "available")
    search_fields = ("title", "isbn")


@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "book",
        "borrow_date",
        "returned",
    )
    list_filter = ("returned",)