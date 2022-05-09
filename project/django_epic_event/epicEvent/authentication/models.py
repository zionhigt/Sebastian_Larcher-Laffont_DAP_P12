from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    manager_id = models.ForeignKey("authentication.User", verbose_name="manager", on_delete=models.SET_NULL, related_name="manager", blank=True, null=True)
    role = models.ForeignKey("authentication.Role", on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["email"], name="unique_user")
        ]

class Role(models.Model):
    name = models.CharField(max_length=25)

    # def __str__(self):
    #     return self.name