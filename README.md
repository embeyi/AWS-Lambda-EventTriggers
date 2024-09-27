# AWS Lambda Event Triggers

This repository explores various ways to trigger AWS Lambda functions and how to utilize variables passed to them.

## Event Sources

1. **Amazon SNS**: Triggers Lambda on message publication. Access the message via the event object.
2. **Amazon SQS**: Invokes Lambda on message arrival in the queue. Extract message attributes from the event object.
3. **Amazon S3**: Triggers Lambda on object creation/deletion. Use bucket name and object key from the event.
4. **Amazon DynamoDB**: Invokes Lambda on item changes via DynamoDB Streams. Access old and new item values in the event.
5. **API Gateway**: Triggers Lambda on HTTP requests. Access query parameters and request body from the event.
6. **CloudWatch Events**: Invokes Lambda on scheduled or resource change events. Utilize the detail field from the event.

## Using Variables in Lambda

When triggered, AWS passes an event object to the Lambda function. Access properties as needed:

```python
def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']  # For SNS
    print(f"Received message: {message}")
```
