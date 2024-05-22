import boto3
import json

# Replace 'your_server_id' with the actual ID of your Transfer server
SERVER_ID = 's-2245b08aaeb0439ab'
# Replace 'your_sns_topic_arn' with the actual ARN of your SNS topic
SNS_TOPIC_ARN = 'arn:aws:sns:region:account-id:your-sns-topic'

def stop_transfer_server(server_id):
    """
    Stop an AWS Transfer Family server.

    Parameters:
    - server_id: The ID of the server to stop.
    """
    # Initialize the Transfer client
    transfer_client = boto3.client('transfer')

    # Stop the server
    response = transfer_client.stop_server(ServerId=server_id)
    print("Server stopped successfully.")

def send_sns_notification(topic_arn, message):
    """
    Send an SNS notification.

    Parameters:
    - topic_arn: The ARN of the SNS topic.
    - message: The message to send.
    """
    # Initialize the SNS client
    sns_client = boto3.client('sns')

    # Publish the message to the SNS topic
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=message
    )
    print("SNS notification sent successfully.")

def lambda_handler(event, context):
    try:
        # Call the function to stop the server
        stop_transfer_server(SERVER_ID)

        # Prepare success message
        success_message = f"Server {SERVER_ID} stopped successfully."
        send_sns_notification(SNS_TOPIC_ARN, success_message)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "Server": str(SERVER_ID),
                "Message": success_message
            })
        }
    except Exception as err:
        # Prepare error message
        error_message = f"Failed to stop server {SERVER_ID}. Error: {str(err)}"
        send_sns_notification(SNS_TOPIC_ARN, error_message)

        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "Server": str(SERVER_ID),
                "Message": error_message
            })
        }
