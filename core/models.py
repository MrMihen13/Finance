from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email', db_index=True, unique=True)
    username = models.CharField(verbose_name='Username', db_index=True, max_length=255, unique=True)
    first_name = models.CharField(verbose_name='First Name', max_length=30)
    last_name = models.CharField(verbose_name='Last Name', max_length=150)
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    is_staff = models.BooleanField(verbose_name='Is Staff', default=False)
    created_at = models.DateTimeField(verbose_name='Created t', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Update at', auto_now=True)
    telegram_id = models.CharField(verbose_name='Telegram ID', max_length=128, blank=True, null=True)
    discord_id = models.CharField(verbose_name='Discord ID', max_length=128, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name', blank=False, null=False)
    limit = models.DecimalField(verbose_name='Limit', max_digits=12, decimal_places=2, blank=True, null=True)
    user_id = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Cost(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name', blank=False, null=False)
    amount = models.DecimalField(verbose_name='Amount', max_digits=12, decimal_places=2, blank=True, null=True)
    category_id = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



