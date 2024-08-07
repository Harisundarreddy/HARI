from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

# Create your models here.


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='api_users',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='api_users',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )