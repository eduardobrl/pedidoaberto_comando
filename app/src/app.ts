import { Prisma, StatusPedido } from '@prisma/client';
import express, { Express, Handler, Request, Response } from 'express';
import { prismaStart, prismaClient} from './infra/prisma/prisma_connector';

const app: Express = express();
app.use(express.json());


app.get('/', (req: Request, res: Response) => {
    res.send('GET Express + TypeScript Server');
});

app.post('/pedido', (req: Request, res: Response) => {
    const pedido : Prisma.PedidoCreateInput = req.body;

    prismaClient.pedido.create({data:{
        status: StatusPedido.ABERTO
    }})
    res.send('POST Express + TypeScript Server');
});


app.post('/produto', async (req: Request, res: Response) => {
    const produto : Prisma.ProdutoCreateInput = req.body;
    console.log(produto)

    try {
        const client = prismaClient;
        await client.produto.create({data:{
            nome:"Teste", 
            quantidadeEstoque:10,
            sku:"123456789",
            valor: 100.5,
            
        }})
      } catch (e) {
        if (e instanceof Prisma.PrismaClientKnownRequestError) {
          // The .code property can be accessed in a type-safe manner
          if (e.code === 'P2002') {
            console.log(
              'There is a unique constraint violation, a new user cannot be created with this email'
            )
          }
        }
        throw e
      }

    res.send("POST Express + TypeScript Server");
});


if(process.env.RUN_LOCAL === "TRUE")
{
    prismaStart();
    app.listen("3000", () => {
        console.log(`Example app listening on port 3000`)
    })
}


export default app;
