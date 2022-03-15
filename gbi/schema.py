from django.contrib.auth.models import User as UserModel
from graphene import Field, ObjectType, Union
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

    icon_object_1 = IconObject()
    icon_object_2 = IconObject()

    def resolve_icon_object_1(parent, info):
        return parent.icon1_object

    def resolve_icon_object_2(parent, info):
        return parent.icon2_object


class Query(ObjectType):
    notifications = DjangoListField(Notification)
