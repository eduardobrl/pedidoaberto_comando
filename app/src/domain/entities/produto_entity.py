from decimal import Decimal
from src.domain.decorators.dynamodataclass import dynamodataclass


@dynamodataclass
class DimensoesProduto:
    """Dimensões do Produto"""
    peso_produto: int
    altura_produto: int
    largura_produto: int
    profundidade_produto: int

@dynamodataclass
class Produto:
    """Classe com dados do produto"""
    id_produto: str
    nome_produto: str
    valor_produto: Decimal
    sku_produto: str
    dimensoes_produto: DimensoesProduto
    quantidade_produto: int = 0