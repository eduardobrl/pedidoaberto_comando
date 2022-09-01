import app from '../../app'
import express, { Express, Handler, Request, Response } from 'express';

import IController from './icontroller';

class PedidoController implements IController{
    constructor(private app : Express){ }

    public register():Express
    {
        app.get('/', (req: Request, res: Response) => {
            res.send('GET Express + TypeScript Server');
        });

        app.post('/', (req: Request, res: Response) => {
            res.send('POST Express + TypeScript Server');
        });

        return app
    }
}


export default PedidoController