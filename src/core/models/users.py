from django.db import models
from src.core.models.constants import CONSTANTS
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    role = models.CharField(max_length=50, choices=CONSTANTS.ROLE.CHOICES, default=CONSTANTS.ROLE.DEFAULT)

    def __str__(self):
        return f"{self.username} - {self.role}"

    class Meta:
        db_table = "users"
        verbose_name = "User"
