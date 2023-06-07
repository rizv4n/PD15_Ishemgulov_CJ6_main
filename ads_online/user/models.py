from django.db import models
from django.contrib.auth.models import AbstractUser

from user.managers import UserManager


class UserRoles(models.TextChoices):
    USER = 'user', 'Пользователь'
    ADMIN = 'admin', 'Администратор'


class User(AbstractUser):

    objects = UserManager()

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12, null=True)
    role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.USER)
    image = models.ImageField(upload_to='user_pic', blank=True, null=True)
    is_admin = False

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    @property
    def is_superuser(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_staff(self):
        return self.role == UserRoles.USER

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username
