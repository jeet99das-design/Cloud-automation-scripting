import boto3
from config import AMI_ID
from config import INSTANCE_TYPE
from config import KEY_NAME
from logger import logger
from upload_logs import upload_logs
ec2 = boto3.resource('ec2')
try:
    instances = ec2.create_instances(
        ImageId=AMI_ID,
        MinCount=1,
        MaxCount=1,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME
    )
    instance = instances[0]
    print(f"Created EC2 Instance: {instance.id}")
    logger.info(f"Created EC2 instance {instance.id}")
    upload_logs()
except Exception as e:
    logger.error(f"Error creating EC2 instance: {e}")
    upload_logs()
    print("Error:", e)
