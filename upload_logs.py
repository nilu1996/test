import boto3

def lambda_handler(event, context):
    # Create EC2 client
    ec2_client = boto3.client('ec2')
    sns_client = boto3.client('sns')
    
    # Get all instances in the region
    instances = ec2_client.describe_instances()
    
    # Initialize a list to store instances with status other than 'running'
    instances_not_running = []
    
    # Check each instance's status
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            # Check if instance state is not 'running'
            if state != 'running':
                instances_not_running.append(instance_id)
    
    # If there are instances not running, trigger an email
    if instances_not_running:
        # Create SNS client
        sns_client = boto3.client('sns')
        
        # Set up the email subject and message
        subject = "EC2 Instance(s) Not Running"
        message = f"The following EC2 instance(s) are not running: {', '.join(instances_not_running)}"
        
        # Publish the message to the specified SNS topic
        sns_client.publish(
            TopicArn='arn:aws:sns:us-east-1:211125567787:test-lambda',
            Message=message,
            Subject=subject
        )
