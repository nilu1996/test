import boto3
import json

# Replace 'your_server_id' with the actual ID of your Transfer server
SERVER_ID = 's-2245b08aaeb0439ab'

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

def lambda_handler(event, context):

    try:
        # Call the function to start the server
        start_transfer_server(SERVER_ID)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "Server ": str(SERVER_ID),
                "Status": "Started"
            })
        }
    except Exception as err:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "Server ": str(SERVER_ID),
                "Error": str(err)
            })
        }
