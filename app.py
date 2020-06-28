#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk_test.aws_cdk_test_stack import AwsCdkTestStack


app = core.App()
AwsCdkTestStack(app, "aws-cdk-test")

app.synth()
