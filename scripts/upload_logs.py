import boto3
from config import S3_BUCKET_NAME
s3 = boto3.client('s3')
def upload_logs():
    try:
        s3.upload_file(
            'logs/cloudops.log',
            S3_BUCKET_NAME,
            'cloudops.log'
        )
        print("Logs uploaded to S3")
    except Exception as e:
        print("Error uploading logs:", e)
