from django.contrib import admin

from product_alias.models import ProductAlias


@admin.register(ProductAlias)
class ProductAliasAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "name",
        "sku_quantity",
        "created_at",
        "updated_at",
    )
