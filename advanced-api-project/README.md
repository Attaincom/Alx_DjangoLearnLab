## API Unit Tests

All tests are located in `api/test_views.py`.

- CRUD operations for Book model are tested.
- Permissions tested: unauthenticated users cannot create/update/delete books.
- Authenticated users can perform all write operations.
- Tests use Django's test database and `APITestCase`.

### Run tests
```bash
python manage.py test api
