import express, { Express, Handler, Request, Response } from 'express';
interface IController {
    register(app: Express): Express
}

export default IController;