#This sample is showing how to process Response output

import boto3
import os

ec2_id = os.environ['InstanceID'] 
ec2 = boto3.resource('ec2')
ec2_instance = ec2.Instance(ec2_id)
ec2_client = boto3.client('ec2')

def ec2_status():
    
    #print('This is the instance id = ' + ec2_id)
    response = ec2_client.describe_instance_status(InstanceIds=[ec2_id])
    instance_status = response['InstanceStatuses'][0]['InstanceStatus']['Status']
    #print('Instance status is ' + instance_status)
    print(response) # This will return "dict" output
    print(response['InstanceStatuses']) #This will return "list" 
    #print(response['InstanceStatuses'][0])
    #print(response['InstanceStatuses'][0]['InstanceStatus'])
    print(response['InstanceStatuses'][0]['InstanceStatus']['Status']) #This return string , based on Boto3 documentation
    print(response['InstanceStatuses'][0]['InstanceStatus']['Details'])
    # [{'Name': 'reachability', 'Status': 'passed'}]
    print(response['InstanceStatuses'][0]['InstanceStatus']['Details'][0])
    # {'Name': 'reachability', 'Status': 'passed'}
    print(response['InstanceStatuses'][0]['InstanceStatus']['Details'][0]['Name'])
    # reachability
    
    
    
def lambda_handler(event, context):
    # TODO implement
    ec2_status()
    return 'Complete'
