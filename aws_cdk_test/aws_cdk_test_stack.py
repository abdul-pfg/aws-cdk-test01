from aws_cdk import core
import aws_cdk.aws_s3 as s3


class AwsCdkTestStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(self,
    		"BucketCDK", 
    		versioned=True,
    		bucket_name='cdk-managed-bucket-s843971',
            removal_policy=core.RemovalPolicy.DESTROY)
        
