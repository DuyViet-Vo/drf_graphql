import graphene
from graphql_jwt.decorators import login_required

from product_alias.models import ProductAlias
from product_alias.types import ProductAliasType
from products.models import Product


class Query(graphene.ObjectType):
    product_alias = graphene.Field(ProductAliasType, id=graphene.Int())
    all_product_aliases = graphene.List(ProductAliasType)

    @login_required
    def resolve_product_alias(self, info, id):
        return ProductAlias.objects.get(pk=id)

    @login_required
    def resolve_all_product_aliases(self, info):
        return ProductAlias.objects.all()


class CreateProductAlias(graphene.Mutation):
    product_alias = graphene.Field(ProductAliasType)

    class Arguments:
        product_id = graphene.ID(required=True)
        name = graphene.String(required=True)
        sku_quantity = graphene.Int(required=True)

    @login_required
    def mutate(self, info, product_id, name, sku_quantity):
        product = Product.objects.get(pk=product_id)
        product_alias = ProductAlias.objects.create(
            product=product, name=name, sku_quantity=sku_quantity
        )
        return CreateProductAlias(product_alias=product_alias)


class UpdateProductAlias(graphene.Mutation):
    product_alias = graphene.Field(ProductAliasType)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        sku_quantity = graphene.Int()

    @login_required
    def mutate(self, info, id, name=None, sku_quantity=None):
        product_alias = ProductAlias.objects.get(pk=id)

        if name:
            product_alias.name = name
        if sku_quantity:
            product_alias.sku_quantity = sku_quantity

        product_alias.save()
        return UpdateProductAlias(product_alias=product_alias)


class DeleteProductAlias(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    @login_required
    def mutate(self, info, id):
        product_alias = ProductAlias.objects.get(pk=id)
        product_alias.delete()
        return DeleteProductAlias(success=True)


class Mutation(graphene.ObjectType):
    create_product_alias = CreateProductAlias.Field()
    update_product_alias = UpdateProductAlias.Field()
    delete_product_alias = DeleteProductAlias.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
