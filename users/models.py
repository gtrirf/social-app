from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):
    date_birth = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'appusers'

    def __str__(self):
        return self.username