from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "created_at",
        "username",
        "password",
        "is_active",
        "is_admin",
        "address",
    )
