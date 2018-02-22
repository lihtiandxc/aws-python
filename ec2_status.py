## os.environ['YourVar']

import boto3, os

ec2_id = os.environ['InstanceID'] 

def ec2_status():
    
    print("This is the instance id = " + ec2_id)
    

def lambda_handler(event, context):
    # TODO implement
    ec2_status()
    return 'Complete'
