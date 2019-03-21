from datetime import datetime
from dateutil.tz import tzlocal

import boto3
# import json

def lambda_handler(event, context):
    # TODO implement
    now = datetime.now()
    year = str(now.year)
    month = str(now.month)
    today = str(now.day)
    hour = str(now.hour)
    min = str(now.minute)
    sec = str(now.second)
    local_tz = str(datetime.now(tzlocal()))
    
    s3_client = boto3.client('s3')
    filename = today +'-'+ month +'-'+year +'-'+hour +'-'+min +'-'+sec
    print("Logs Started -----")
    print (filename)
    
    s3_client.put_object(Body='hi', Bucket='flatfilesupload',Key=filename)
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda! ' + today +'-'+ month +'-'+year +'-'+hour +'-'+min +'-'+sec)
    #     # 'body': json.dumps(local_tz)
    # }
    print("Logs Ended -----")
