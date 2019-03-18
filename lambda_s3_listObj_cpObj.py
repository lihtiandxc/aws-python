import boto3
import time

start = time.time()
s3_client = boto3.client('s3')
def lambda_handler(event, context):
    print('Logging started')
    SourceBucket = 'flatfilesupload'
    TargetBucket = 'flatfilestorage2'
    
    response = s3_client.list_objects(
        Bucket = SourceBucket,
        Prefix = 'new/')
    key = response['Contents']
    enum_key = list(enumerate(key))
    
    for index, elem in enum_key:
        file = elem['Key']
        # print(file)
        copy_source = {'Bucket':SourceBucket, 'Key':file}
        s3_client.copy_object(Bucket=TargetBucket, Key=file, CopySource=copy_source)
    print('Logging ended')
    end = time.time()
    print(round(end-start, 3))
