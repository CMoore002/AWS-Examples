#!/usr/bin/env python3

import aws_cdk as cdk
from aws_cdk import RemovalPolicy
import aws_cdk.aws_s3 as s3
from cdk.cdk_stack import CdkStack


app = cdk.App()
stack = CdkStack(app, "CdkStack")

## creating s3 bucket
bucket = s3.Bucket(stack, "Bucket")
app.synth()