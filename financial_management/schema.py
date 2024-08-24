# myproject/schema.py
import graphene

from products.schema import Mutation as ProductsMutation
from products.schema import Query as ProductsQuery
from users.schema import Mutation as UsersMutation
from users.schema import Query as UsersQuery


class Query(UsersQuery, ProductsQuery, graphene.ObjectType):
    pass


class Mutation(UsersMutation, ProductsMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
