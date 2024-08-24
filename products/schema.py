import graphene
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required

from .models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    product = graphene.Field(ProductType, id=graphene.Int())

    @login_required
    def resolve_all_products(self, info):
        return Product.objects.all()

    @login_required
    def resolve_product(self, info, id):
        return Product.objects.get(pk=id)


class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()
        price = graphene.Float(required=True)
        stock = graphene.Int(required=True)

    product = graphene.Field(ProductType)

    @login_required
    def mutate(self, info, name, description, price, stock):
        user = info.context.user
        product = Product(
            name=name,
            description=description,
            price=price,
            stock=stock,
            user=user,
        )
        product.save()
        return CreateProduct(product=product)


class UpdateProduct(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)
        description = graphene.String()
        price = graphene.Float(required=True)
        stock = graphene.Int(required=True)

    product = graphene.Field(ProductType)
    message = graphene.String()

    @login_required
    def mutate(self, info, id, name, description, price, stock):
        try:
            product = Product.objects.get(pk=id)
            product.name = name
            product.description = description
            product.price = price
            product.stock = stock
            product.save()
            return UpdateProduct(
                product=product, message="Sản phẩm đã được sửa thành công!"
            )
        except Product.DoesNotExist:
            return UpdateProduct(
                product=None, message="Không tìm thấy sản phẩm."
            )


class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    oke = graphene.Boolean()
    message = graphene.String()

    @login_required
    def mutate(self, info, id):
        try:
            product = Product.objects.get(pk=id)
            product.delete()
            return DeleteProduct(
                oke=True, message="Sản phẩm đã được xóa thành công."
            )
        except Product.DoesNotExist:
            return DeleteProduct(oke=False, message="Không tìm thấy sản phẩm.")


class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
