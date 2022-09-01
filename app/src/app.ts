import express, { Express, Handler, Request, Response } from 'express';

const app: Express = express();

app.post('/', (req: Request, res: Response) => {
    res.send('POST Express + TypeScript Server');
});

export default app;
