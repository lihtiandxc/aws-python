#This lambda function print all the instances from single asg

import boto3
import os

auto_scaling_grp_name = os.environ['asg_name']
asg_client = boto3.client('autoscaling')

def lambda_handler(event, context):
    # TODO implement
    
    response = asg_client.describe_auto_scaling_instances()
    i = 0
    for n in response:
        auto_scaling_instance = response['AutoScalingInstances'][i]['InstanceId']
        i = i + 1
        print(auto_scaling_instance)
        
    return 'Complete'
