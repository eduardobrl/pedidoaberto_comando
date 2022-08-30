from marshmallow_dataclass import dataclass as marshmallow_dataclass

@marshmallow_dataclass
class Cliente:
    id_cliente: str

    nome_cliente: str
    telefone_cliente: str
    email_cliente: str
    documento_cliente: str

    rua_endereco_cliente: str
    cep_endereco_cliente: str
    bairro_endereco_cliente: str
    complemento_endereco_cliente: str