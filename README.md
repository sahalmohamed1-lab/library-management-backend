# Library Management System - Backend

## Overview

This is the Django REST Framework backend for the Library Management System. It provides secure REST APIs for managing books, authors, categories and book borrowing using JWT authentication.

## Features

- User registration
- User login with JWT
- Book management
- Author management
- Category management
- Borrow books
- Return books
- Search books
- Filter books
- Role-based permissions

## Technologies

- Python
- Django
- Django REST Framework
- PostgreSQL / SQLite
- SimpleJWT
- Django Filter

## Installation

Clone the repository

```bash
git clone <repository-url>
cd backend
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Linux/Mac

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Create a superuser

```bash
python manage.py createsuperuser
```

Start the server

```bash
python manage.py runserver
```

The API will run on:

```
http://127.0.0.1:8000/
```

## API Endpoints

### Authentication

- POST `/api/auth/register/`
- POST `/api/auth/login/`
- GET `/api/auth/profile/`

### Authors

- GET `/api/authors/`
- POST `/api/authors/`
- PUT `/api/authors/{id}/`
- DELETE `/api/authors/{id}/`

### Categories

- GET `/api/categories/`
- POST `/api/categories/`
- PUT `/api/categories/{id}/`
- DELETE `/api/categories/{id}/`

### Books

- GET `/api/books/`
- POST `/api/books/`
- PUT `/api/books/{id}/`
- DELETE `/api/books/{id}/`

Supports:

- Search
- Ordering
- Filtering

Example

```
/api/books/?search=python
/api/books/?author=1
/api/books/?category=2
/api/books/?available=true
```

### Borrowing

Borrow a book

```
POST /api/borrow/
```

Return a book

```
POST /api/borrow/return/{id}/
```

My borrowed books

```
GET /api/borrow/my-books/
```

## Permissions

Regular users can:

- View books
- Borrow books
- Return books

Staff users can:

- Manage books
- Manage authors
- Manage categories

## Author

Sahal Mohamed