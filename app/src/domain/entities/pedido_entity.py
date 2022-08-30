import datetime
from decimal import Decimal
from typing import List
from marshmallow_dataclass import dataclass as marshmallow_dataclass
from enum import Enum
from xmlrpc.client import DateTime

from src.domain.entities.cliente_entity import Cliente
from src.domain.entities.produto_entity import DimensoesProduto, Produto


class StatusPedidoEnum(Enum):
    ABERTO = 1
    PAGO = 2
    ENVIADO = 3
    FINALIZADO = 4

@marshmallow_dataclass
class DetalhePedido:
    produto: Produto
    valor_produto: Decimal
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

if __name__=="__main__":
    dimensoes = DimensoesProduto(1,1,1,1)
    produto = Produto("123", "Capacete", 100.56, "4564656ds5sda", dimensoes, 10)
    detalhesPedido = [DetalhePedido(produto, 200, 10)]
    atualizacao = AtualizacaoPedido(StatusPedidoEnum.ABERTO, "Teste", datetime.datetime())
    cliente = Cliente("1","2","3","4","5","6","7","8","9")
    pedido = Pedido("123", "123", detalhesPedido, atualizacao, cliente)

    print(pedido)