import os

import boto3

S3_BUCKET = "lil.sh"
PREFIX = "surl"


def main():
    upload_blank_object()


def upload_blank_object():
    s3 = boto3.client("s3")
    s3.put_object(
        Body=b'',
        Bucket=S3_BUCKET,
        Key=f"surl/hello",
        WebsiteRedirectLocation="https://google.com"
    )


if __name__ == '__main__':
    main()
