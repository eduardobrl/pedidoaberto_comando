import boto3
from boto3.dynamodb.types import TypeSerializer
from boto3_type_annotations.dynamodb import Client
from app.domain.entities.pedido_entity import DetalhePedido, Pedido, StatusPedidoEnum
from app.domain.entities.produto_entity import Produto
from botocore.exceptions import ClientError


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

        deserialised = {k: [v2 for k2, v2 in v.items()][0] for k, v in result.get("Item").items()}
        return Pedido.Schema().load(deserialised)


    def inserir_pedido(self, pedido: Pedido):
        try:
            result = self.client.put_item(
                self.table_name,
                Item={k: serializer.serialize(v) for k, v in Pedido.Schema().dump(pedido).items() if v != ""}
            )
        except ClientError as err:
            raise err

        return result


    