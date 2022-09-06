import { Prisma } from '@prisma/client'
import { prismaClient } from '../../infra/prisma/prisma_connector'

export default async function inserir_pedido(pedido: Prisma.PedidoCreateInput)
{
    return await prismaClient.pedido.create({data:pedido});
}

