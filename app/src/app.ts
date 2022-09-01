import express, { Express, Handler, Request, Response } from 'express';
import addControllers from './infra/controller/controller';

const app: Express = express();

addControllers(app)

export default app;
