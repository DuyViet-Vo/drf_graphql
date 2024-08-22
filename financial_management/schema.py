# myproject/schema.py
import graphene
from users.schema import Query as UsersQuery, Mutation as UsersMutation
from products.schema import Query as ProductsQuery, Mutation as ProductsMutation

class Query(UsersQuery, ProductsQuery, graphene.ObjectType):
    pass

class Mutation(UsersMutation, ProductsMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
