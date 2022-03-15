from graphene import Field, List, ObjectType, String
from graphene_django import DjangoListField, DjangoObjectType

from .models import Author, Book


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ("id", "name")


class Query(ObjectType):
    authors = DjangoListField(AuthorType)
    author_by_id = Field(AuthorType, id=String())

    def resolve_author_by_id(root, info, id):
        return Author.objects.get(pk=id)
