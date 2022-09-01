import { PrismaClient } from "@prisma/client"

let prismaClient : PrismaClient

const prismaStart = () => {
    prismaClient = new PrismaClient();
}

export {prismaStart, prismaClient}