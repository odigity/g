from graphene import Schema, ObjectType, String

import gbi.schema
import librarius.schema


class Query(
    gbi.schema.Query,
#    librarius.schema.Query,
    ObjectType
):
    hello = String(default_value="Hi!")


schema = Schema(query=Query)
