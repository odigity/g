from graphene import Schema, ObjectType, String


class Queries(
    ObjectType
):
    hello = String(default_value="Hi!")


class Mutations(
    ObjectType
):
    pass


schema = Schema(query=Queries, mutation=Mutations)
print(schema)
