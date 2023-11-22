import boto3
import json

# Initialize CloudWatch client
cloudwatch = boto3.client('cloudwatch')

def lambda_handler(event, context):
    # Your FizzBuzz logic here
    result = fizzbuzz_logic(event['number'])  # Assuming fizzbuzz_logic is your function

    # Put a custom metric
    cloudwatch.put_metric_data(
        MetricData = [
            {
                'MetricName': 'FizzBuzzOutput',
                'Dimensions': [
                    {
                        'Name': 'OutputType',
                        'Value': result
                    },
                ],
                'Unit': 'Count',
                'Value': 1
            },
        ],
        Namespace = 'MyFizzBuzzFunction'
    )

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
