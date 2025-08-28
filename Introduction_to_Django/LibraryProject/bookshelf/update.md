# Update

```python
from bookshelf.models import Book
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()

# Verify
Book.objects.get(pk=b.pk).title
# Expected output:
# 'Nineteen Eighty-Four'
