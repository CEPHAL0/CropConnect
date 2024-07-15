from django.db import models


class User(models.Model):

    RoleChoices = models.TextChoices("RoleChoices", "admin user farmer moderator")

    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True, db_index=True)
    email = models.CharField(max_length=100, unique=True, db_index=True)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    role = models.CharField(choices=RoleChoices, max_length=100, default="user")

    class Meta:
        db_table = "users"

