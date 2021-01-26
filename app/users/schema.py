from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.Int(required=True))
    me = graphene.Field(UserType)

    def resolve_user(self, info, id):
        return get_user_model().objects.get(id=id)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('Não esta logado no sistema')
        return user


class AddUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        user = get_user_model().objects.create(
            username=kwargs.get('username'),
            email=kwargs.get('email')
        )
        user.set_password(kwargs.get('password'))
        user.save()

        return AddUser(user=user)


class Mutation:
    add_user = AddUser.Field()
