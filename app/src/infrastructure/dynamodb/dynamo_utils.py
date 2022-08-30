from typing import Any
from marshmallow_dataclass import dataclass as marshmallow_dataclass
from boto3.dynamodb.types import TypeSerializer

class DynamoUtils:
    @staticmethod
    def serializar(entity):
        serialized =  {k: TypeSerializer().serialize(v) for k, v in type(entity).Schema().dump(entity).items() if v != ""}
        return serialized
       
    @staticmethod
    def deserializar(result):
        deserialized = {k: [v2 for k2, v2 in v.items()][0] for k, v in result.get("Item").items()}
        return deserialized