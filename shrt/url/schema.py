import graphene

from graphene_django.types import DjangoObjectType

from shrt.url.models import Url

class UrlType(DjangoObjectType):
    """Simple object mapping."""
    class Meta:
        model = Url


class Query(graphene.ObjectType):
    """Query type to add to the root schema."""
    url = graphene.Field(UrlType,
                         id=graphene.Int(),
                         original=graphene.String(),
                         shortened=graphene.String())
    all_urls = graphene.List(UrlType)

    def resolve_url(self, info, **kwargs):
        id = kwargs.get('id')
        original = kwargs.get('original')
        shortened = kwargs.get('shortened')

        if id is not None:
            return Url.objects.get(pk=id)

        if original is not None:
            return Url.objects.get(original=original)

        if shortened is not None:
            return Url.objects.get(shortened=shortened)

        return None

    def resolve_all_urls(self, info, **kwargs):
        return Url.objects.all()


class CreateUrl(graphene.Mutation):
    """Mutation to handle creating a new URL entry."""
    id = graphene.Int()
    original = graphene.String()
    shortened = graphene.String()

    class Arguments:
        original = graphene.String(required=True)

    def mutate(self, info, original):
        url = Url(original=original)
        url.save()

        return Url(
            id=url.id,
            original=url.original,
            shortened=url.shortened
        )


class Mutation(graphene.ObjectType):
    """Mutation type to add to the root schema."""
    create_url = CreateUrl.Field()
