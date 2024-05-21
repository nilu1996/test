import boto3
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        # Define your EC2 region
        ec2_region = 'us-east-1'

        # Initialize the EC2 client
        ec2_client = boto3.client('ec2', region_name=ec2_region)

        # List of instance IDs to start
        instance_ids = ['i-0834b38f7628b7a6c']

        # Start each instance
        for instance_id in instance_ids:
            try:
                response = ec2_client.start_instances(InstanceIds=[instance_id])
                logger.info(f"Start Instances Response: {response}")
                logger.info(f"Started EC2 instance: {instance_id}")
            except Exception as e:
                logger.error(f"Error starting instance {instance_id}: {str(e)}")

        logger.info("All specified EC2 instances have been processed.")
        
    except Exception as e:
        logger.error(f"Lambda function error: {str(e)}")

# Uncomment the following lines to test locally
# if __name__ == "__main__":
#     lambda_handler(None, None)
