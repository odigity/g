from django.contrib.auth.models import User as UserModel

from graphene        import Field, ObjectType, Schema, String, Union
from graphene_django import DjangoListField, DjangoObjectType

from . import models


class User(DjangoObjectType):
    class Meta:
        model = UserModel
        fields = ("id",)


class Advisor(DjangoObjectType):
    class Meta:
        model = models.Advisor
        fields = ("id", "user", "full_name", "avatar")


class Investor(DjangoObjectType):
    class Meta:
        model = models.Investor
        fields = ("id", "user", "full_name", "avatar")


class PlanCategory(DjangoObjectType):
    class Meta:
        model = models.PlanCategory
        fields = ("id", "label", "icon")


class Plan(DjangoObjectType):
    class Meta:
        model = models.Plan
        fields = ("id", "name", "category")


class IconObject(Union):
    class Meta:
        types = (Advisor, Investor, Plan)


class Notification(DjangoObjectType):
    class Meta:
        model = models.Notification
        fields = ("id", "body")

    icon1_object = IconObject()
    icon2_object = IconObject()


class Queries(ObjectType):
    hello         = String(default_value="Hi!")
    notifications = DjangoListField(Notification)


class Mutations(ObjectType):
    pass


#schema = Schema(query=Queries, mutation=Mutations)
schema = Schema(query=Queries)
#print(schema)
