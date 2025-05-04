from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="email",
        help_text="Формат почты user@mail.ru"
    )
    phone = models.CharField(
        max_length=30,
        verbose_name="телефон",
        help_text="Формат номера телефона 8 888 888 88 88",
        **NULLABLE
    )
    token = models.CharField(
        max_length=70,
        verbose_name="token",
        **NULLABLE
    )
    first_name = models.CharField(
        max_length=200,
        verbose_name='Имя',
        **NULLABLE
    )
    patronymic = models.CharField(
        max_length=200,
        verbose_name='Отчество',
        **NULLABLE
    )
    last_name = models.CharField(
        max_length=200,
        verbose_name='Фамилиля',
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
