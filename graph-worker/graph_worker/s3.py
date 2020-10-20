import boto3

import config

client = boto3.client('s3')

def upload_image(img: str, ticker: str, timeframe: str, ext: str) -> dict:
    response = client.put_object(
        ACL='public-read',
        Body=img,
        Bucket=config.S3_BUCKET,
        Key=f'stock-{ticker}-{timeframe}.{ext}'
    )

    return response