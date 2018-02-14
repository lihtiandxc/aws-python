import boto3

client = boto3.client('ec2')

def lambda_handler(event, context):
    # TODO implement
    
    ec2_api = 'dxcsb-a-vir-configmng'
    
    response = client.describe_instances(Filters=[{'Name':'tag:Name' ,'Values':[ec2_api]}])
    #response = client.describe_instances()
    for reservation in response['Reservations']:
        
        for instance in reservation['Instances']:
            
            #print(instance['InstanceId'])
            print(instance['ImageId'])
            for network in instance['NetworkInterfaces']:
                print(network['NetworkInterfaceId'])
    

    return 'Complete'
