
---

### 📕 `delete.md`

```markdown
## 🔹 Delete the Book

```python
from bookshelf.models import Book

# Delete the book instance
book.delete()

# Confirm deletion
Book.objects.all()
# <QuerySet []>
