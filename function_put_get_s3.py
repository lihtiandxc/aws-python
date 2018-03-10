import boto3
import json


#Write file and put into s3 with specifi path
data = {"HelloWorld" : []}
s3res = boto3.resource('s3')
obj = s3res.Object('limliht-config','config/us-east-1/3/10/hello.json')
#obj.put(Body=json.dumps(data))

#read file from s3

read_data = obj.get()['Body'].read()
print(read_data)
