# myproject/schema.py
import graphene

from product_alias.schema import Mutation as ProductAliasMutation
from product_alias.schema import Query as ProductAliasQuery
from products.schema import Mutation as ProductsMutation
from products.schema import Query as ProductsQuery
from users.schema import Mutation as UsersMutation
from users.schema import Query as UsersQuery


class Query(ProductAliasQuery, UsersQuery, ProductsQuery, graphene.ObjectType):
    pass


class Mutation(
    ProductAliasMutation, UsersMutation, ProductsMutation, graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
