from aws_lambda_typing import context as context_, events


def lambda_handler(event: events.APIGatewayProxyEventV2, context: context_.Context) -> None :
    message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])  
    return { 
        'message' : message
    }