from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name: str):
    try:
        author = Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        print(f"No author named '{author_name}' found.")
        return
    
    # Required filter usage
    qs = Book.objects.filter(author=author).values_list("title", flat=True)
    
    print(f"\nBooks by {author_name}:")
    for title in qs:
        print(f" - {title}")


def books_in_library(library_name: str):
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print(f"No library named '{library_name}' found.")
        return
    
    qs = library.books.all().values_list("title", "author__name")
    print(f"\nBooks in '{library_name}':")
    for title, author_name in qs:
        print(f" - {title} (by {author_name})")


def librarian_for_library(library_name: str):
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print(f"No library named '{library_name}' found.")
        return

    try:
        # 👇 explicit get() with filter condition
        librarian = Librarian.objects.get(library=library)
        print(f"\nLibrarian for '{library_name}': {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"\nNo librarian assigned to '{library_name}'.")


if __name__ == "__main__":
    books_by_author("Chinua Achebe")
    books_in_library("City Central Library")
    librarian_for_library("City Central Library")
