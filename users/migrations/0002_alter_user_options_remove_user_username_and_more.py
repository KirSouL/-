# Generated by Django 4.1.1 on 2025-05-04 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="user",
            name="patronymic",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Отчество"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True,
                help_text="Формат номера телефона 8 888 888 88 88",
                max_length=30,
                null=True,
                verbose_name="телефон",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="token",
            field=models.CharField(
                blank=True, max_length=70, null=True, verbose_name="token"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                help_text="Формат почты user@mail.ru",
                max_length=254,
                unique=True,
                verbose_name="email",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Имя"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Фамилиля"
            ),
        ),
    ]
