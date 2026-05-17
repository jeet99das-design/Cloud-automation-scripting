import boto3
from logger import logger
from upload_logs import upload_logs
ec2 = boto3.client('ec2')
try:
    response = ec2.describe_instances()
    instances = []
    print("\nEC2 INSTANCES:\n")
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            print(f"{len(instances)+1}. {instance_id} | {state}")
            instances.append({
                "id": instance_id,
                "state": state
            })
    choice = int(input("\nSelect instance number: "))
    selected = instances[choice - 1]
    instance_id = selected["id"]
    state = selected["state"]
    if state == "running":
        ec2.stop_instances(
            InstanceIds=[instance_id]
        )
        print(f"\nStopped instance: {instance_id}")
        logger.info(
            f"Stopped instance {instance_id}"
        )
    elif state == "stopped":
        ec2.start_instances(
            InstanceIds=[instance_id]
        )
        print(f"\nStarted instance: {instance_id}")
        logger.info(
            f"Started instance {instance_id}"
        )
    else:
        print(f"\nInstance is in '{state}' state.")
        logger.info(
            f"Skipped instance {instance_id} because state is {state}"
        )
    upload_logs()
except Exception as e:
    logger.error(f"Error toggling EC2 instance: {e}")
    upload_logs()
    print("Error:", e)
