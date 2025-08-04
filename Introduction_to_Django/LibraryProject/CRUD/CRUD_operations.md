

````markdown
# 📚 Django CRUD Operations for Book Model

This document contains all the basic Create, Retrieve, Update, and Delete (CRUD) operations performed on the `Book` model using Django ORM in the shell.

---

## ✅ Create

```python
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

book
# <Book: 1984 by George Orwell>
````

---

## 🔍 Retrieve

```python
from bookshelf.models import Book

# Retrieve the book by title
book = Book.objects.get(title="1984")

book.title
# '1984'

book.author
# 'George Orwell'

book.publication_year
# 1949
```

---

## ✏️ Update

```python
# Assuming you already retrieved the book
book.title = "Nineteen Eighty-Four"
book.save()

book.title
# 'Nineteen Eighty-Four'
```

---

## 🗑️ Delete

```python
# Delete the book instance
book.delete()

# Confirm deletion
Book.objects.all()
# <QuerySet []>
```

---

````
