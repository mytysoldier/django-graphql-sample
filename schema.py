import graphene
import graphqlapp.schema

class Query(graphqlapp.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(
    query=Query
)