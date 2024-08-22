# users/schema.py
import graphene
from .models import CustomUser
from graphene_django.types import DjangoObjectType
from django.contrib.auth import authenticate
import graphql_jwt

# Define CustomUser model type
class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser


# Define Query
class Query(graphene.ObjectType):
    user = graphene.Field(CustomUserType, id=graphene.Int())
    all_users = graphene.List(CustomUserType)

    def resolve_user(self, info, id):
        return CustomUser.objects.get(pk=id)

    def resolve_all_users(self, info):
        return CustomUser.objects.all()


# Define Mutation
class RegisterCustomUser(graphene.Mutation):
    user = graphene.Field(CustomUserType)

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        address = graphene.String(required=False)

    def mutate(self, info, username, email, password, address=None):
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            address=address,
        )
        return RegisterCustomUser(user=user)


class Mutation(graphene.ObjectType):
    register_user = RegisterCustomUser.Field()
