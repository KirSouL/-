from django.contrib import admin
from users.models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'phone',
        'first_name',
        'patronymic',
        'last_name',
    )
    list_filter = (
        'email',
        'first_name',
        'patronymic',
        'last_name',
    )
    search_fields = (
        'email',
        'phone',
        'first_name',
        'patronymic',
        'last_name',
    )
