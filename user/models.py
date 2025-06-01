from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from .base import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text=_("The groups this user belongs to. A user will get all permissions granted to each of their groups."),
        verbose_name=_("groups"),
        related_name='user_groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text=_("Specific permissions for this user."),
        verbose_name=_("user permissions"),
        related_name='user_permissions',
    )

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email