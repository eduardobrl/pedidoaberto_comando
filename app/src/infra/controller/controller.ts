import PedidoController from './pedido_controller'
import express, { Express, Handler, Request, Response } from 'express';

export default function addControllers(app : Express){
    new PedidoController(app).register();
}