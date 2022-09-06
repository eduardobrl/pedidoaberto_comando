import { PrismaClient } from "@prisma/client"
import { SecretsManager, SSM } from "aws-sdk"
import Contants  from '../../domain/constants/constants'
let prismaClient : PrismaClient

const prismaStart = async () => {

    let connectionString = process.env.DATABASE_URL;
    if(connectionString == null)
    {
        var ssm = new SSM({region:"sa-east-1"});
        const data = await ssm.getParameter({Name:Contants.SSM_CONFIG_CONNECTION_STRING, WithDecryption:true}).promise()
        connectionString = data.Parameter?.Value
    }

    prismaClient = new PrismaClient({
        datasources: {
          db: {
            url: connectionString
          },
        },
      });
}

export {prismaStart, prismaClient}