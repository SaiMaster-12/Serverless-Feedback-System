import json
import boto3
import uuid
from datetime import datetime
import os

dynamodb = boto3.resource('dynamodb')
ses = boto3.client('ses')

# These must match your Lambda environment variables
TABLE_NAME = os.environ['TABLE_NAME']
ADMIN_EMAIL = os.environ['ADMIN_EMAIL']

def lambda_handler(event, context):
    try:
        # Parse the JSON body
        body = json.loads(event['body'])
        user_email = body['userEmail']
        message = body['feedbackMessage']

        # Generate a unique ID and timestamp
        feedback_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()

        # Write to DynamoDB
        table = dynamodb.Table(TABLE_NAME)
        table.put_item(Item={
            'feedbackId': feedback_id,
            'userEmail': user_email,
            'feedbackMessage': message,
            'timestamp': timestamp
        })

        # Send email via SES
        ses.send_email(
            Source=ADMIN_EMAIL,
            Destination={'ToAddresses': [ADMIN_EMAIL]},
            Message={
                'Subject': {'Data': 'New Feedback Received'},
                'Body': {
                    'Text': {
                        'Data': (
                            f"From: {user_email}\n\n"
                            f"Message:\n{message}\n\n"
                            f"Received at: {timestamp}"
                        )
                    }
                }
            }
        )

        # Return success response with CORS headers
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({'message': 'Feedback submitted successfully.'})
        }

    except Exception as e:
        print("Error:", str(e))
        # Return error response with CORS headers
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({'error': 'Internal Server Error'})
        }
