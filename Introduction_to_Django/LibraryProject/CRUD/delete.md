## 🔹 Delete the Book

```python
from bookshelf.models import Book

# Retrieve the book (required before deletion)
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book instance
book.delete()

# Confirm deletion
Book.objects.all()
# <QuerySet []>
