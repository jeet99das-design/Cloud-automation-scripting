import boto3
from logger import logger
from upload_logs import upload_logs
ec2 = boto3.client('ec2')
try:
    response = ec2.describe_instances()
    print("\nEC2 INSTANCES:\n")
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            print(f"{instance_id} | {state}")
    logger.info("Listed EC2 instances")
    upload_logs()
except Exception as e:
    logger.error(f"Error listing EC2 instances: {e}")
    upload_logs()
    print("Error:", e)
