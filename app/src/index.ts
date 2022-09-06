import app from './app'
import dotenv from 'dotenv';
import {configure} from '@vendia/serverless-express'
import {prismaStart, prismaClient} from './infra/prisma/prisma_connector'
dotenv.config();

let serverlessExpressInstance: any

async function asyncTask () {
    await prismaStart()
}
  
async function setup (event:any, context:any) {
    const asyncValue = await asyncTask()
    serverlessExpressInstance = configure({ app })
    return serverlessExpressInstance(event, context)
}
  
async function handler (event:any, context:any) {
    if (serverlessExpressInstance) return serverlessExpressInstance(event, context)
    return await setup(event, context)
}
  
exports.handler = handler