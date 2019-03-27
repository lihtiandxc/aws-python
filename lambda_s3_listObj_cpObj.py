import boto3
import time
import logging
from botocore.exceptions import ClientError
from datetime import datetime

start = time.time()
s3_res = boto3.resource('s3')

def lambda_handler(event, context):

    now = datetime.now()
    month = str(now.month)
    day = str(now.day)
    hour = str(now.hour)
    min = str(now.minute)
    sec = str(now.second)

    LogginID = '[' + month+day+hour+min+sec + ']'
    print(LogginID + 'Logging started')

    SourceBucketName = 'flatfilesupload'
    TargetBucketName = 'flatfilestorage2'
    SourceBucket = s3_res.Bucket(SourceBucketName)
    TargetBucket = s3_res.Bucket(TargetBucketName)
    KeyList = []

    try:
        SourceObjs = SourceBucket.objects.filter(Prefix='new/')
        for SourceObj in SourceObjs:
            KeyList.append(SourceObj.key)
        if len(KeyList) == 0:
            print('No Object Found')
        else:
            # print(SourceObj.key)
            StrSourceObj = str(SourceObj.key)
            copy_source = {
                'Bucket': SourceBucketName,
                'Key': StrSourceObj
            }
            TargetObj = TargetBucket.Object(StrSourceObj)
            TargetObj.copy(copy_source)
        print(str(KeyList))
    except ClientError as e:
        logging.error(e)

    print(LogginID + 'Logging ended')
    end = time.time()
    TimeSpent = str(round(end-start, 3))
    print(LogginID + '' + TimeSpent)
