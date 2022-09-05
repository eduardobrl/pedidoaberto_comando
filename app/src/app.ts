import express, { Express, Handler, Request, Response } from 'express';
import { env } from 'process';
import { prismaStart } from './infra/prisma/prisma_connector';

const app: Express = express();

app.get('/', (req: Request, res: Response) => {
    res.send('GET Express + TypeScript Server');
});

app.post('/', (req: Request, res: Response) => {
    res.send('POST Express + TypeScript Server');
});

if(process.env.RUN_LOCAL === "TRUE")
{
    prismaStart();
    app.listen("3000", () => {
        console.log(`Example app listening on port 3000`)
    })
}


export default app;
