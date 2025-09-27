from django.db import models

class Author(models.Model):
    """
    Author model stores details of book authors.
    One Author can have many Books (one-to-many relationship).
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model stores details of books.
    Each book belongs to one Author (via ForeignKey).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
