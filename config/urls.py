from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("library.urls.auth_urls")),
    path("api/authors/", include("library.urls.author_urls")),
    path("api/categories/", include("library.urls.category_urls")),
    path("api/books/", include("library.urls.book_urls")),
    path("api/borrow/", include("library.urls.borrow_urls")),
    path("api/dashboard/", include("library.urls.dashboard_urls")),
]