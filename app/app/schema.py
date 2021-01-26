import graphene
import core.schema
import users.schema
import graphql_jwt


class Query(core.schema.Query, users.schema.Query, graphene.ObjectType):
    pass


class Mutation(core.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
