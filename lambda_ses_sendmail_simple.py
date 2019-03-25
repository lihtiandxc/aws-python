import json
import boto3

client = boto3.client('ses')

def lambda_handler(event, context):
    response = client.send_email(
        Destination={
            'ToAddresses': [
                'your-verified@email.com'  #for AWS SES Sandbox account, recipients email has to be verified as well https://docs.aws.amazon.com/ses/latest/DeveloperGuide/request-production-access.html
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': 'UTF-8',
                    'Data': 'This message body contains HTML formatting. It can, for example, contain links like this one: <a class="ulink" href="http://docs.aws.amazon.com/ses/latest/DeveloperGuide" target="_blank">Amazon SES Developer Guide</a>.',
                },
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': 'This is the message body in text format.',
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Test email',
            },
        },
        ReplyToAddresses = [''],
        ReturnPath='your-verified@email.com',
        ReturnPathArn='arn:aws:ses:us-east-1:1234567890:identity/your-verified@email.com',
        Source='your-verified@email.com',
        SourceArn='arn:aws:ses:us-east-1:1234567890:identity/your-verified@email.com',
    )
    
    print(response)
