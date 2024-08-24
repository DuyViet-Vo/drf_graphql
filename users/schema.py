import graphene
from django.contrib.auth import get_user_model
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required
from graphql_jwt.shortcuts import get_token

User = get_user_model()


class CustomUserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email", "address", "created_at")


class Register(graphene.Mutation):
    user = graphene.Field(CustomUserType)
    token = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        address = graphene.String(required=False)

    def mutate(self, info, username, password, email, address=None):
        user = User(
            username=username,
            email=email,
            address=address,
        )
        user.set_password(password)
        user.save()

        token = get_token(user)
        return Register(user=user, token=token)


class ObtainToken(graphene.Mutation):
    token = graphene.String()
    user = graphene.Field(CustomUserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise Exception("Invalid credentials")
            token = get_token(user)
            return ObtainToken(token=token, user=user)
        except User.DoesNotExist:
            raise Exception("User not found")


class Query(graphene.ObjectType):
    me = graphene.Field(CustomUserType)

    @login_required
    def resolve_me(self, info):
        user = info.context.user
        return user


class Mutation(graphene.ObjectType):
    register = Register.Field()
    obtain_token = ObtainToken.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
