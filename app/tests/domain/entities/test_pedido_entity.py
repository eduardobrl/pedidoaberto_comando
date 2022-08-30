import datetime
import pytest
from src.domain.decorators.dynamodataclass import dynamodataclass
from src.domain.entities.cliente_entity import Cliente
from src.domain.entities.pedido_entity import AtualizacaoPedido, DetalhePedido, Pedido, StatusPedidoEnum
from src.domain.entities.produto_entity import DimensoesProduto, Produto
from datetime import date

def test_pedido():
    dimensoes = DimensoesProduto(1,1,1,1)
    produto = Produto("123", "Capacete", 100.56, "4564656ds5sda", dimensoes, 10)
    detalhesPedido = [DetalhePedido(produto, 200, 10)]
    atualizacao = [AtualizacaoPedido(StatusPedidoEnum.ABERTO, "Teste", date.today())]
    cliente = Cliente("1","2","3","4","5","6","7","8","9")
    pedido = Pedido("123", "123", detalhesPedido, atualizacao, cliente)


    print(pedido.serialize(Pedido, pedido))

    assert True