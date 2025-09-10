
---

## Combined CRUD log (CRUD_operations.md)
Create a single file `CRUD_operations.md` that shows the whole session (concatenate the four sections above, formatted as a shell session). Example:

```markdown
# CRUD Operations (Django shell)

```python
>>> from bookshelf.models import Book

# CREATE
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book
<Book: 1984>

# RETRIEVE
>>> Book.objects.all()
<QuerySet [<Book: 1984>]>
>>> b = Book.objects.get(title="1984")
>>> b.title, b.author, b.publication_year
('1984', 'George Orwell', 1949)

# UPDATE
>>> b.title = "Nineteen Eighty-Four"
>>> b.save()
>>> Book.objects.get(pk=b.pk).title
'Nineteen Eighty-Four'

# DELETE
>>> b.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>
