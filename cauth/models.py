from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


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
        user.rate_plan = 'pro'
        user.save()

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):  # TODO Тесты авторизации
    RATE_PlANS = [('free', 'Бесплатный'), ('base', 'Базовый'), ('professional', 'Профессиональный')]

    email = models.EmailField(verbose_name='Email', db_index=True, unique=True)
    username = models.CharField(verbose_name='Username', db_index=True, max_length=255, unique=True)
    first_name = models.CharField(verbose_name='First Name', max_length=30)
    last_name = models.CharField(verbose_name='Last Name', max_length=150)

    rate_plan = models.CharField(verbose_name='Rate plan', choices=RATE_PlANS, max_length=13,
                                 default='free')  # TODO Предусмотреть добавление пробного периода

    telegram_uid = models.CharField(verbose_name='Telegram ID', max_length=128, blank=True, null=True)

    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    is_staff = models.BooleanField(verbose_name='Is Staff', default=False)
    created_at = models.DateTimeField(verbose_name='Created t', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Update at', auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
