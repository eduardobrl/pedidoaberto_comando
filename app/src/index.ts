import { Context, APIGatewayProxyResult, APIGatewayEvent } from 'aws-lambda';
import app from './app'
import dotenv from 'dotenv';
import {configure} from '@vendia/serverless-express'
import {prismaStart, prismaClient} from './infra/prisma/prisma_connector'
dotenv.config();

let serverlessExpressInstance: any

function asyncTask () {
    prismaStart()
}
  
function setup (event:any, context:any) {
    const asyncValue = asyncTask()
    serverlessExpressInstance = configure({ app })
    return serverlessExpressInstance(event, context)
}
  
function handler (event:any, context:any) {
    if (serverlessExpressInstance) return serverlessExpressInstance(event, context)
    return setup(event, context)
}
  
exports.handler = handler