import graphene

from graphene_django.types import DjangoObjectType

from shrt.url.models import Url

class UrlType(DjangoObjectType):
    """Simple object mapping."""
    class Meta:
        model = Url


class Query(graphene.ObjectType):
    """Query type to add to the root schema.

    Allows querying by ID, tag, and shortened URL if they exist.

    Attributes:
        url (Field): Query type representing the URL model for single response.
        all_urls (List): A list of URL objects for responding with all entities.
    """
    url = graphene.Field(UrlType,
                         id=graphene.Int(),
                         tag=graphene.String(),
                         shortened=graphene.String())
    all_urls = graphene.List(UrlType)

    def resolve_url(self, info, **kwargs):
        id = kwargs.get('id')
        tag = kwargs.get('tag')
        shortened = kwargs.get('shortened')

        if id is not None:
            return Url.objects.get(pk=id)

        if tag is not None:
            return Url.objects.get(tag=tag)

        if shortened is not None:
            return Url.objects.get(shortened=shortened)

        return None

    def resolve_all_urls(self, info, **kwargs):
        return Url.objects.all()


class CreateUrl(graphene.Mutation):
    """Mutation to handle creating a new URL entry.

    Attributes:
        id (int): ID of the entity that was created.
        original (str): The full URL given to shorten.
        shortened (str): The shortened URL including host and tag.
    """
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


class DeleteUrl(graphene.Mutation):
    """Mutation to handle deleting a URL entry.

    Attributes:
        id (int): ID of the entity to delete.
    """
    id = graphene.Int()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        url = Url.objects.get(pk=id)
        url.delete()

        return Url(
            id=id
        )


class Mutation(graphene.ObjectType):
    """Mutation type to add to the root schema."""
    create_url = CreateUrl.Field()
    delete_url = DeleteUrl.Field()