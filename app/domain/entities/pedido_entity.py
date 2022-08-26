from ast import List
from marshmallow_dataclass import dataclass as marshmallow_dataclass
from enum import Enum
from xmlrpc.client import DateTime
from app.domain.entities.cliente_entity import Cliente
from app.domain.entities.produto_entity import Produto

class StatusPedidoEnum(Enum):
    ABERTO = 1
    PAGO = 2
    ENVIADO = 3
    FINALIZADO = 4

@marshmallow_dataclass
class DetalhePedido:
    produto: Produto
    valor_produto: float
    quantidade: int

@marshmallow_dataclass
class AtualizacaoPedido:
    status_atualizacao: StatusPedidoEnum
    motivo_atualizacao: str
    data_hora_atualizacao: DateTime

@marshmallow_dataclass
class Pedido:
    """Pedidos realizados por usuário do sistema"""
    id_pedido: str
    id_usuario: str
    detalhes_pedido: List[DetalhePedido]
    atualizacoes_pedido: List[AtualizacaoPedido]
    cliente_pedido: Cliente