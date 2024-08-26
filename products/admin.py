from django.contrib import admin

from products.models import Product


@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "name",
        "description",
        "price",
        "stock",
        "created_at",
        "updated_at",
    )
