import os
import boto3

#asg_name = os.environ['asg_name']
asg_name = 'limliht-asg,limliht2-asg'
list_asg_name = asg_name.split(',')
asg_client = boto3.client('autoscaling')
ec2_client = boto3.client('ec2')

#def evaluation():
    #get event network id 
    #compare with the network id list
    #publish sns topic

def get_nw_id_from_ec2(ec2_id):
    
    response_ec2 = ec2_client.describe_instances(InstanceIds=ec2_id)
    ec2_list = response_ec2['Reservations']
    
    list_network_int_id = []
    
    for ec2_group in ec2_list:
        #print(ec2s['Instances'])
        ec2s = ec2_group['Instances']
        
        for ec2 in ec2s:
            network_int_id = (ec2['NetworkInterfaces'][0]['NetworkInterfaceId'])
            list_network_int_id.append(network_int_id)
    
    #return list_network_int_id
    print(list_network_int_id)


def get_ec2_id_from_asg():
    
    response_asg = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=list_asg_name)
    #print(response_asg['AutoScalingGroups'])
    asg_list  = response_asg['AutoScalingGroups']
    # print(type(response_asg['AutoScalingGroups']))
    # print(len(response_asg['AutoScalingGroups']))
    
    list_instance = []
    
    for asg in asg_list:
        
        #print(asg['AutoScalingGroupName'])
        instances = asg['Instances']
        
        for instance in instances:
            instance_id = instance['InstanceId']
            list_instance.append(instance_id)
        
    #print(list_instance)
    
    return list_instance
        

def lambda_handler(event, context):
    # TODO implement
    
    returned_ec2_id = get_ec2_id_from_asg()
    #get_ec2_id_from_asg()
    get_nw_id_from_ec2(returned_ec2_id)

    return 'Success'
