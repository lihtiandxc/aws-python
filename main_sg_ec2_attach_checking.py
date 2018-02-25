###------- Author : lih-tian.lim@dxc.com
###------- Version : 1.0
###------- Title : Function to trigger email notification whenever any security group
###-------         attach/detach activity on Instances

from datetime import datetime
import boto3
import json
import logging
import sys

LOGGER = logging.getLogger()
for h in LOGGER.handlers:
    LOGGER.removeHandler(h)

HANDLER = logging.StreamHandler(sys.stdout)
FORMAT = '%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'
HANDLER.setFormatter(logging.Formatter(FORMAT))
LOGGER.addHandler(HANDLER)
LOGGER.setLevel(logging.INFO)

###------- 
#event_network_id = 'eni-c0614e3d'  #simulate event passing nw id string
#str_asg_name = 'limliht-asg,limliht2-asg' #simulate global var in lambda
#global_asg_name = str_asg_name.split(',')
service_tag_name = 'Service'
service_tag = 'account'
env_tag_name = 'Env'
env_tag = 'production'

sns_topic_arn = 'arn:aws:sns:us-east-1:751611215147:limliht_topic2'

###-------
ec2_resource = boto3.resource('ec2')
sns_client = boto3.client('sns')

###-------
def get_instance_id(network_id):
    
    network_interface = ec2_resource.NetworkInterface(network_id)
    instance_id = network_interface.attachment['InstanceId']
    result = instance_id
    return result
    
###-------    
def get_instance_tag(ec2_id):
    
    instance = ec2_resource.Instance(ec2_id)
    tagging = instance.tags
    
    for value in tagging:
        if value['Key'] == env_tag_name and value['Value'] == env_tag:
            for instance_value in tagging:
                if instance_value['Key'] == service_tag_name \
                and instance_value['Value'] == service_tag :
                    
                    get_instance_tag_result = instance_value['Value'].upper() + 'PF EC2 ' + \
                    ' with instance id ' +  ec2_id
                    print(get_instance_tag_result)
                    
                    return get_instance_tag_result
                else:
                    pass
        else:
            pass

###-------                    
def sns_result(e, ec2_details, network_id):

        
    details = e['detail']['eventName']
    accesskey_id =  e['detail']['userIdentity']['accessKeyId']
    username = e['detail']['userIdentity']['userName']
    event_id = e['detail']['eventID']
    aws_region = e['detail']['awsRegion']
    source_ip =  e['detail']['sourceIPAddress']
    user_agent = e['detail']['userAgent']
    parameters = e['detail']['requestParameters']['groupSet']['items']
    sg_parameters = json.dumps(parameters)

    str_e = json.dumps(e)
    str_e_data = json.loads(str_e)
    event_time_json = str_e_data['detail']['eventTime']
    event_time_datetime_format = str(datetime.strptime(event_time_json, '%Y-%m-%dT%H:%M:%SZ'))
        
    construct_msg = 'Event log: \
    \n\nEvent name : ' + details + \
    '\nEvent Id : ' + event_id + \
    '\nEvent time (UTC) : ' + event_time_datetime_format + \
    '\nUser Access Key : ' + accesskey_id + \
    '\nUsername : ' + username + \
    '\nAWS Region : ' + aws_region + \
    '\nSource IP : ' + source_ip + \
    '\nUser agent : ' + user_agent + \
    '\nSecurity Group information : ' + sg_parameters

    if details == 'ModifyNetworkInterfaceAttribute':
        event_json = json.dumps(e)
        subject_msg = 'Security Group has changed on this '+ ec2_details
        sns_client.publish(TargetArn = sns_topic_arn, MessageStructure = 'string', \
        Message = construct_msg, Subject = subject_msg)
    
    else:
        pass

###-------
def lambda_handler(event, context):
    # TODO implement
    
    event_network_id = event['detail']['requestParameters']['networkInterfaceId']
    print(event_network_id)
 
    try: 
        returned_instance_id = get_instance_id(event_network_id)
        returned_instance_tag = get_instance_tag(returned_instance_id)
        if returned_instance_tag is not None:
            sns_result(event, returned_instance_tag, event_network_id)
        else:
            pass
    except  Exception as error:
        LOGGER.exception(error)
    
    return 'Success!'
