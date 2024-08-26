from graphene_django.types import DjangoObjectType

from product_alias.models import ProductAlias


class ProductAliasType(DjangoObjectType):
    class Meta:
        model = ProductAlias
        fields = (
            "id",
            "product",
            "name",
            "sku_quantity",
            "created_at",
            "updated_at",
        )
