import boto3
from logger import logger
from upload_logs import upload_logs
ec2 = boto3.client('ec2')
try:
    response = ec2.describe_instances()
    logger.info("Scheduled task started")
    print("\nEC2 STATUS REPORT:\n")
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            print(f"{instance_id} | {state}")
            logger.info(
                f"Instance {instance_id} is {state}"
            )
    upload_logs()
    logger.info("Scheduled task completed")
except Exception as e:
    logger.error(f"Scheduled task error: {e}")
    upload_logs()
    print("Error:", e)
