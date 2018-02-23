import boto3
import os
import logging
import sys
import json

LOGGER = logging.getLogger()
for h in LOGGER.handlers:
    LOGGER.removeHandler(h)
    
HANDLER = logging.StreamHandler(sys.stdout)
FORMAT = '%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'
HANDLER.setFormatter(logging.Formatter(FORMAT))
LOGGER.addHandler(HANDLER)
LOGGER.setLevel(logging.INFO)

## global var ##
ec2_id = os.environ['InstanceID']
sns_topic_arn = os.environ['sns_topic_arn']
sns_client = boto3.client('sns')

## ec2 boto3 module ##
ec2 = boto3.resource('ec2')
ec2_instance = ec2.Instance(ec2_id)
ec2_client = boto3.client('ec2')

## function get ec2 status ## 
def ec2_status():
    
    #print('This is the instance id = ' + ec2_id)
    response = ec2_client.describe_instance_status(InstanceIds=[ec2_id])
    instance_status = response['InstanceStatuses'][0]['InstanceStatus']['Status']
    

    print(instance_status)
    

    if instance_status == 'ok':
        LOGGER.info('Aborts. EC2 Status is ok')
        
        return
    else:
        LOGGER.info('EC2 status is not ok')

def lambda_handler(event, context):
    # TODO implement
    try:
        #if (event['detail']['eventName'] == 'ModifyNetworkInterfaceAttribute' and event['detail']['requestParameters']['networkInterfaceId'] == os.environ['en_id']):
        #     sns_client.publish(TargetArn = sns_topic_arn, Message = event, Subject = 'This is a test email from limliht_test_lambda')
        event_details = event['detail']['eventName']
        event_network_id = event['detail']['requestParameters']['networkInterfaceId']
        print(event_details)
        print(event_network_id)
        event_json = json.dumps(event)
        if event_details == 'ModifyNetworkInterfaceAttribute' and event_network_id == os.environ['en_id']:
            sns_client.publish(TargetArn = sns_topic_arn, MessageStructure = 'json', Message = json.dumps({'default' : event_json}), Subject = 'This is a test email from limliht_test_lambda')
        
        ec2_status()
    except Exception as error:
        LOGGER.exception(error)
    return 'Complete'
