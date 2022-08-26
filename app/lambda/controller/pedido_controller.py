
from app.domain.entities.pedido_entity import Pedido

def obter_pedido_por_id(id: str) -> Pedido:
    pedido = Pedido()
    return pedido