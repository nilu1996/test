import boto3
import json

# Replace 'your_server_id' with the 
# actual ID of your Transfer server
SERVER_ID = 'your_server_id'

def stop_transfer_server(server_id):
    """
    Stop an AWS Transfer Family server.

    Parameters:
    - server_id: The ID of the server to stop.
    """
    # Initialize the Transfer client
    transfer_client = boto3.client('transfer')


    response = transfer_client.stop_server(ServerId=server_id)
    print("Server stopped successfully.")

def lambda_handler(event, context):

    try:
        # Call the function to stop the server
        stop_transfer_server(SERVER_ID)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "Server ": str(SERVER_ID)
            })
        }
    except Exception as err:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "Server ": str(SERVER_ID)
            })
        }
