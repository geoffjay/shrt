import graphene

from graphene_django.types import DjangoObjectType

from shrt.url.models import Url

class UrlType(DjangoObjectType):
    class Meta:
        model = Url


class Query(graphene.ObjectType):
    url = graphene.Field(UrlType,
                         id=graphene.Int(),
                         name=graphene.String(),
                         shortened=graphene.String())
    all_urls = graphene.List(UrlType)

    def resolve_url(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        shortened = kwargs.get('shortened')

        if id is not None:
            return Url.objects.get(pk=id)

        if name is not None:
            return Url.objects.get(name=name)

        if shortened is not None:
            return Url.objects.get(shortened=shortened)

        return None

    def resolve_all_urls(self, info, **kwargs):
        return Url.objects.all()


class CreateUrl(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()

    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, name):
        url = Url(name=name)
        url.save()

        return Url(
            id=url.id,
            name=url.name
        )


class Mutation(graphene.ObjectType):
    create_url = CreateUrl.Field()
