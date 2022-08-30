import datetime
import boto3
from boto3.dynamodb.types import TypeSerializer
from boto3_type_annotations.dynamodb import Client
from botocore.exceptions import ClientError
from app.src.infrastructure.dynamodb.dynamo_utils import DynamoUtils

from src.domain.entities.pedido_entity import Pedido


serializer = TypeSerializer()

class PedidoRepository:
    def __init__(self) -> None:
        self.client: Client = boto3.client('dynamodb')
        self.table_name: str = ""

    def obter_pedido_por_id(self, id_pedido: str, id_usuario: str) -> Pedido:
        try:
            result = self.client.get_item(
                self.table_name,
            )
        except ClientError as err:
            raise err

        return DynamoUtils.deserializar(result)


    def inserir_pedido(self, pedido: Pedido):
        try:
            result = self.client.put_item(
                self.table_name,
                Item=DynamoUtils.serializar(pedido)
            )
        except ClientError as err:
            raise err

        return result

    def atualizar_status_pedido(self, pedido: Pedido):
        try:
            result = self.client.update_item(
                self.table_name,
                Item={k: serializer.serialize(v) for k, v in Pedido.Schema().dump(pedido).items() if v != ""}
            )
        except ClientError as err:
            raise err

        return result