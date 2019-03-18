import boto3
import time

start = time.time()
s3_client = boto3.client('s3')
def lambda_handler(event, context):
    print('Logging started')
    response = s3_client.list_objects(
        Bucket = 'flatfilesupload',
        Prefix = 'new/') # with prefix
    key = response['Contents']
    enum_key = list(enumerate(key))
    
    for index, elem in enum_key:
        print(elem['Key'])
        
    print('Logging ended')
    end = time.time()
    print(round(end-start, 3))
