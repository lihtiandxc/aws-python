import boto3
import time
import logging
from datetime import datetime
from botocore.exceptions import ClientError


start = time.time()
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    
    now = datetime.now()
    month = str(now.month)
    day = str(now.day)
    hour = str(now.hour)
    min = str(now.minute)
    sec = str(now.second)

    LogginID = '[' + month+day+hour+min+sec + ']'
    
    print(LogginID + 'Logging started')
    
    SourceBucket = 'flatfilesupload'
    TargetBucket = 'flatfilestorage2'
    KeyList = []
    
    response = s3_client.list_objects(
        Bucket = SourceBucket,
        Prefix = 'new/')
    try:
        key = response['Contents'] #Processing Array
    except Exception as e:
        # raise e
        logging.error('No Object Found')
        # return False # return function here will terminate the program if it is False
    else:    
        enum_key = list(enumerate(key))
        # return True
    
    for index, elem in enum_key:
        file = str(elem['Key'])
        KeyList.append(file)
        copy_source = {'Bucket':SourceBucket, 'Key':file}
        s3_client.copy_object(Bucket=TargetBucket, Key=file, CopySource=copy_source)
    print(KeyList)
    
    print(LogginID + 'Logging ended')
    end = time.time()
    TimeSpent = str(round(end-start, 3))
    print(LogginID + '' + TimeSpent)
