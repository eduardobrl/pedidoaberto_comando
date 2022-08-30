from aws_lambda_typing import context as context_, events


def lambda_handler(event: events.APIGatewayProxyEventV2, context: context_.Context) -> None :

    return event