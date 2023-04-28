from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_cognito as cognito,
    aws_s3 as s3,
    aws_secretsmanager as secrets,
    core,
)

class MicroserviceStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, service_name: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Lambda function
        lambda_function = _lambda.Function(
            self, f"{service_name}_function",
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.asset("path/to/lambda/code"),
            handler="handler.main",
        )

        # API Gateway
        api = apigw.LambdaRestApi(
            self, f"{service_name}_api",
            handler=lambda_function,
            rest_api_name=f"{service_name}_api",
        )

        # Cognito User Pool
        user_pool = cognito.UserPool(
            self, f"{service_name}_user_pool",
            user_pool_name=f"{service_name}_user_pool",
        )

        # S3 bucket for frontend hosting
        s3_bucket = s3.Bucket(
            self, f"{service_name}_frontend",
            bucket_name=f"{service_name}-frontend",
            website_index_document="index.html",
            website_error_document="error.html",
            public_read_access=True,
        )

        # Secrets Manager
        api_key_secret = secrets.Secret(
            self, f"{service_name}_api_key",
            secret_name=f"{service_name}_api_key",
            generate_secret_string=secrets.SecretStringGenerator(
                exclude_characters="/@\"'",
            ),
        )

        # Outputs
        core.CfnOutput(
            self, f"{service_name}_api_url",
            value=api.url,
            description=f"{service_name} API Gateway URL",
        )

        core.CfnOutput(
            self, f"{service_name}_user_pool_id",
            value=user_pool.user_pool_id,
            description=f"{service_name} Cognito User Pool ID",
        )

        core.CfnOutput(
            self, f"{service_name}_frontend_bucket",
            value=s3_bucket.bucket_name,
            description=f"{service_name} Frontend S3 Bucket",
        )
