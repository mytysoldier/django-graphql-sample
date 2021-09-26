import graphene
import graphqlapp.schema

class Query(graphqlapp.schema.Query, graphene.ObjectType):
    pass

class Mutation(graphqlapp.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)

