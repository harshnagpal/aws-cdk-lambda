#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk_lambda.aws_cdk_lambda_stack import AwsCdkLambdaStack


app = cdk.App()
AwsCdkLambdaStack(app, "aws-cdk-lambda")

app.synth()
