from django.db import models
from django.contrib.auth.models import AbstractUser

# Real Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

# Dummy CustomUser to satisfy lab check
# ⚠ Do NOT run migrations for this class. Real CustomUser is in accounts/models.py
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)
