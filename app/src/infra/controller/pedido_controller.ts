import app from '../../app'
import express, { Express, Handler, Request, Response } from 'express';

app.get('/', (req: Request, res: Response) => {
    res.send('GET Express + TypeScript Server');
});

app.post('/', (req: Request, res: Response) => {
    res.send('POST Express + TypeScript Server');
});

