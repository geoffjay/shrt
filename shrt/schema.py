import graphene

import shrt.url.schema

class Query(shrt.url.schema.Query, graphene.ObjectType):
    """Root query."""
    pass


class Mutation(shrt.url.schema.Mutation, graphene.ObjectType):
    """Root mutation."""
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
