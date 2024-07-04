import json
import os

def lambda_handler(event, context):
    # Sample API keys for validation (these should be securely stored and managed)
    valid_api_keys = os.environ['VALID_API_KEYS'].split(',')

    # Extract API key from the request
    api_key = event['headers'].get('x-api-key')

    if api_key in valid_api_keys:
        return {
            'statusCode': 200,
            'body': json.dumps('API Key is valid')
        }
    else:
        return {
            'statusCode': 401,
            'body': json.dumps('Unauthorized')
        }
