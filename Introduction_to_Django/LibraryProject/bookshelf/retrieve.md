
---

### 📗 `retrieve.md`

```markdown
## 🔹 Retrieve the Book

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
