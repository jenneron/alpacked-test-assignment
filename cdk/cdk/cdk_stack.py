from aws_cdk import (
    core as cdk,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
)

class CdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "jenneron-contentful-bucket")

        cloudfront_distribution = cloudfront.CloudFrontWebDistribution(
            self,
            "jenneron-contentful",
            origin_configs=[
                cloudfront.SourceConfiguration(
                    s3_origin_source=cloudfront.S3OriginConfig(
                        s3_bucket_source=bucket,
                    ),
                    behaviors=[
                        cloudfront.Behavior(
                            is_default_behavior=True,
                        )
                    ],
                )
            ],
        )
