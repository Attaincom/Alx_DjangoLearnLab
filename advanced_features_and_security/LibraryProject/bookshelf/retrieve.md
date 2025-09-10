# Retrieve

```python
from bookshelf.models import Book
# Retrieve all books
Book.objects.all()
# Expected output:
# <QuerySet [<Book: 1984>]>

# Retrieve the specific book
b = Book.objects.get(title="1984")
b.title, b.author, b.publication_year
# Expected output:
# ('1984', 'George Orwell', 1949)
