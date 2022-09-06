terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.48.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.1.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.2.0"
    }
  }

  backend "remote" {
    organization = "pedidoaberto"

    workspaces {
      name = "pedidoaberto_comando"
    }
  }

  required_version = "~> 1.0"
}

provider "aws" {
  region = var.myregion
}


# Lambda
resource "aws_lambda_function" "api_handler" {
  filename      = "app.zip"
  function_name = "${var.app_name}-${var.microservice_name}-lambda"
  role          = aws_iam_role.role.arn
  handler       = "index.handler"
  runtime       = "nodejs14.x"
  timeout       = 30
  memory_size   = 512

  source_code_hash = filebase64sha256("app.zip")
}


# API Gateway
resource "aws_api_gateway_rest_api" "api" {
  name = "${var.app_name}-${var.microservice_name}-api"
}

resource "aws_api_gateway_resource" "resource" {
  path_part   = "{any+}"
  parent_id   = aws_api_gateway_rest_api.api.root_resource_id
  rest_api_id = aws_api_gateway_rest_api.api.id
}

resource "aws_api_gateway_method" "method" {
  rest_api_id          = aws_api_gateway_rest_api.api.id
  resource_id          = aws_api_gateway_resource.resource.id
  http_method          = "ANY"
  authorization        = "COGNITO_USER_POOLS"
  authorizer_id        = aws_api_gateway_authorizer.api_authorizer.id
  authorization_scopes = ["aws.cognito.signin.user.admin"]
}

resource "aws_api_gateway_integration" "lambda_function_gtw_integration" {
  rest_api_id             = aws_api_gateway_rest_api.api.id
  resource_id             = aws_api_gateway_resource.resource.id
  http_method             = aws_api_gateway_method.method.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.api_handler.invoke_arn
}

resource "aws_cloudwatch_log_group" "api_gw" {
  name = "/aws/api_gw/${aws_api_gateway_rest_api.api.name}"

  retention_in_days = 30
}

resource "aws_lambda_permission" "api_gw" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.api_handler.function_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_rest_api.api.execution_arn}/*/*"
}

resource "aws_api_gateway_deployment" "api_gw" {
  rest_api_id = aws_api_gateway_rest_api.api.id

  triggers = {
    redeployment = sha1(jsonencode([
      aws_api_gateway_rest_api.api.id,
      aws_api_gateway_authorizer.api_authorizer.id,
      aws_api_gateway_integration.lambda_function_gtw_integration.id,
    ]))
  }


  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_api_gateway_authorizer" "api_authorizer" {
  name        = "${var.app_name}-${var.microservice_name}-fornecedor"
  rest_api_id = aws_api_gateway_rest_api.api.id
  type          = "COGNITO_USER_POOLS"
  provider_arns = ["arn:aws:cognito-idp:sa-east-1:525636320068:userpool/sa-east-1_uK0Mj9ISA"]
}

resource "aws_api_gateway_stage" "dev_stage" {
  deployment_id = aws_api_gateway_deployment.api_gw.id
  rest_api_id   = aws_api_gateway_rest_api.api.id
  stage_name    = "dev"
}

# IAM
resource "aws_iam_role" "role" {
  name = "myrole"
  managed_policy_arns = [
    "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
    "arn:aws:iam::aws:policy/AmazonSSMReadOnlyAccess"]
  assume_role_policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
POLICY
}