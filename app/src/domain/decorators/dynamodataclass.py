from typing import Any
from marshmallow_dataclass import dataclass as marshmallow_dataclass
from boto3.dynamodb.types import TypeSerializer

def dynamodataclass(foo):

    def serialize(entity, eddntity, obj):
        serialized =  {k: TypeSerializer().serialize(v) for k, v in entity.Schema().dump(obj).items() if v != ""}
        return serialized


    def decorator():
        marshmallow = marshmallow_dataclass(foo)
        marshmallow.serialize = serialize
        return marshmallow

    return decorator()

class AttributeValue():
    def __init__(self, marshmalow) -> None:
        self.serializer = TypeSerializer()
        self.entity = marshmalow

    def serialize(self, obj):
        serialized =  {k: self.serializer.serialize(v) for k, v in self.entity.Schema().dump(obj).items() if v != ""}
        return serialized

    def deserialize(obj, result):   
        deserialized = {k: [v2 for k2, v2 in v.items()][0] for k, v in result.get("Item").items()}
        return deserialized