import { Context, APIGatewayProxyResult, APIGatewayEvent } from 'aws-lambda';
import express, { Express, Request, Response } from 'express';
import dotenv from 'dotenv';

dotenv.config();

const app: Express = express();

app.get('/', (req: Request, res: Response) => {
    res.send('Express + TypeScript Server');
});
  