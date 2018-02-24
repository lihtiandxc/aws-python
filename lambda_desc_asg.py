import os
import boto3

asg_name = os.environ['asg_name']
list_asg_name = asg_name.split(',')

def get_ec2_id_from_asg():
    
    asg_client = boto3.client('autoscaling')
    response_asg = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=list_asg_name)
    #print(response_asg['AutoScalingGroups'])
    asg_list  = response_asg['AutoScalingGroups']
    # print(type(response_asg['AutoScalingGroups']))
    # print(len(response_asg['AutoScalingGroups']))
    
    for asg in asg_list:
        
        print(asg['AutoScalingGroupName'])
        instances = asg['Instances']
        
        list_instance = []
        
        for instance in instances:
            instance_id = instance['InstanceId']
            list_instance.append(instance_id)
        
        #print(list_instance)
        return list_instance

def lambda_handler(event, context):
    # TODO implement
    


    return 'Success'
