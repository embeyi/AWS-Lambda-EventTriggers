import json

def lambda_handler(event, context):
    print(' Hi SQS Triggerred me')
    # Loop through each record in the event
    for record in event['Records']:
        # Extract the body of the SQS message 
        message_body = record['body']
        
        # Print the entire message body
        print("Message Body:", message_body)
        
        # If the message body is JSON formatted, you can parse it
        try:
            message = json.loads(message_body)
            print("Parsed Message:", json.dumps(message, indent=2))
        except json.JSONDecodeError:
            print("Message is not in JSON format.")

    return {
        'statusCode': 200,
        'body': json.dumps('Processed SQS messages')
    }
