import os
import boto3

asg_name = os.environ['asg_name']
list_asg_name = asg_name.split(',')

def lambda_handler(event, context):
    # TODO implement
    
    asg_client = boto3.client('autoscaling')
    response_asg = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=list_asg_name)
    #print(response_asg['AutoScalingGroups'])
    asg_list  = response_asg['AutoScalingGroups']
    # print(type(response_asg['AutoScalingGroups']))
    # print(len(response_asg['AutoScalingGroups']))
    
    for asg in asg_list:
        
        print(asg['AutoScalingGroupName'])
        instances = asg['Instances']
        
        for instance in instances:
            print(instance['InstanceId'])

    return 'Success'
