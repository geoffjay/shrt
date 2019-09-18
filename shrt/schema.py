import graphene

import shrt.url.schema

class Query(shrt.url.schema.Query, graphene.ObjectType):
    pass


class Mutation(shrt.url.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
