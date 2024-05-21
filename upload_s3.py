import boto3

def lambda_handler(event, context):
    # Define your EC2 region
    ec2_region = 'us-east-1'

    # Initialize the EC2 client
    ec2_client = boto3.client('ec2', region_name=ec2_region)

    # List of instance IDs to start
    instance_ids = ['i-0834b38f7628b7a6c']

    # Start each instance
    for instance_id in instance_ids:
        response = ec2_client.start_instances(InstanceIds=[instance_id])
        print(response)
        print(f"Started EC2 instance: {instance_id}")

    print("All specified EC2 instances have been started.")
