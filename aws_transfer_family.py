import boto3
import json

# Replace 'your_server_id' with the actual ID of your Transfer server
SERVER_ID = 's-2245b08aaeb0439ab'
# Replace with your SNS topic ARN
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:090124397890:Instance-Health-monitoring'

def start_transfer_server(server_id):
    """
    Start an AWS Transfer Family server.

    Parameters:
    - server_id: The ID of the server to start.
    """
    # Initialize the Transfer client
    transfer_client = boto3.client('transfer')

    response = transfer_client.start_server(ServerId=server_id)
    print("Server started successfully.")

def send_sns_notification(subject, message):
    """
    Send a notification via SNS.

    Parameters:
    - subject: The subject of the SNS message.
    - message: The message body of the SNS message.
    """
    sns_client = boto3.client('sns')
    response = sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=subject,
        Message=message
    )
    print("SNS notification sent.")

def lambda_handler(event, context):

    try:
        # Call the function to start the server
        start_transfer_server(SERVER_ID)

        # Prepare success message
        success_message = json.dumps({
            "Server": str(SERVER_ID),
            "Status": "Started"
        })

        # Send success notification
        send_sns_notification("Server Started Successfully", success_message)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": success_message
        }
    except Exception as err:
        # Prepare error message
        error_message = json.dumps({
            "Server": str(SERVER_ID),
            "Error": str(err)
        })

        # Send error notification
        send_sns_notification("Server Start Failed", error_message)

        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": error_message
        }
