import boto3
import time
import logging
from datetime import datetime
# from botocore.exceptions import ClientError


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
    
    print(LogginID,'Logging started')
    
    SourceBucket = 'limliht-pli'
    TargetBucket = 'limliht-pli2'
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
        copy = s3_client.copy_object(Bucket=TargetBucket, Key=file, CopySource=copy_source)
        # print(copy) # This can show out the copy_object metadata
        # print(copy['ResponseMetadata']['HTTPStatusCode'])
        # Sample metadata {'ResponseMetadata': {'RequestId': 'D678C7AE611FA43D', 'HostId': 'rxLOvrP69PgsmesUbNIPWeBivgquDg3Jj1bOwoOZrgolnzJiYviqWIAg4WyajL4ciS4ux/88muc=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'rxLOvrP69PgsmesUbNIPWeBivgquDg3Jj1bOwoOZrgolnzJiYviqWIAg4WyajL4ciS4ux/88muc=', 'x-amz-request-id': 'D678C7AE611FA43D', 'date': 'Thu, 28 Mar 2019 04:23:35 GMT', 'x-amz-copy-source-version-id': 'FTTDsYBYZjSegBYJwoU44spfPuy0r0Ut', 'x-amz-version-id': 'o6CBS4QzWj8GLOrXkWlkm0cMXVdX2qwO', 'content-type': 'application/xml', 'content-length': '234', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'CopySourceVersionId': 'FTTDsYBYZjSegBYJwoU44spfPuy0r0Ut', 'VersionId': 'o6CBS4QzWj8GLOrXkWlkm0cMXVdX2qwO', 'CopyObjectResult': {'ETag': '"49f68a5c8493ec2c0bf489821c21fc3b"', 'LastModified': datetime.datetime(2019, 3, 28, 4, 23, 35, tzinfo=tzlocal())}}
        if copy['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(file,'Copy operation successed')
        else:
            print(file,'Copy operation failed')
    print(KeyList)
    
    print(LogginID,'Logging ended')
    end = time.time()
    TimeSpent = str(round(end-start, 3))
    print(LogginID,TimeSpent)

