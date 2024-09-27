import json

def lambda_handler(event, context):
    # Log the received event
    print("Received event: " + json.dumps(event, indent=2))
    
    # Iterate over SNS records
    for record in event['Records']:
        sns_message = record['Sns']['Message']
        sns_subject = record['Sns']['Subject']
        sns_timestamp = record['Sns']['Timestamp']
        
        # Print SNS message details
        print(f"SNS Message: {sns_message}")
        print(f"SNS Subject: {sns_subject}")
        print(f"SNS Timestamp: {sns_timestamp}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Message processed successfully')
    }
