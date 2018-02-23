import boto3
import os


auto_scaling_grp_name = os.environ['asg_name']
asg_client = boto3.client('autoscaling')
ec2_client = boto3.client('ec2')

    
def desc_asg_instance():
    
    response = asg_client.describe_auto_scaling_instances()
    auto_scaling_instances = response['AutoScalingInstances'] #Return a List
    enum_auto_scaling_instances = list(enumerate(auto_scaling_instances)) #enumerate is python build in function https://docs.python.org/3/library/functions.html#enumerate
    #print(enum_auto_scaling_instances)
    
    total_instances = len(auto_scaling_instances) # count the item in a List
    
    for index, elem in enum_auto_scaling_instances:
        ec2_instance_id = elem['InstanceId']
        #print('This is the Instance ID = ' + ec2_instance_id)
        response_ec2 = ec2_client.describe_instances(InstanceIds=[ec2_instance_id])
        #print(response_ec2)
        ec2_details = response_ec2['Reservations'][0]['Instances'][0] #[0] this is helping to to convert the List to Dict from boto3 Response
        ec2_nw_interface = ec2_details['NetworkInterfaces'][0]
        ec2_nw_int_id = ec2_nw_interface['NetworkInterfaceId']
        #print(ec2_details)
        #print(ec2_nw_interface)
        print('This is the ec2 ' + ec2_instance_id + ' interface id = ' + ec2_nw_int_id)
        
        

def desc_ec2_nw_interface(nw_id):
    
    response = ec2_client.describe_network_interface_attribute(Attribute = 'attachment', NetworkInterfaceId = nw_id)
#    print(response)
    

def lambda_handler(event, context):
    # TODO implement

    desc_asg_instance()
    #desc_ec2_nw_interface()

    return 'Complete'
