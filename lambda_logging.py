#This sample has the logging module. 

import boto3
import os
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

## global var ##
ec2_id = os.environ['InstanceID']

## ec2 boto3 module ##
ec2 = boto3.resource('ec2')
ec2_instance = ec2.Instance(ec2_id)
ec2_client = boto3.client('ec2')

## function get ec2 status ## 
def ec2_status():
    
    #print('This is the instance id = ' + ec2_id)
    response = ec2_client.describe_instance_status(InstanceIds=[ec2_id])
    instance_status = response['InstanceStatuses'][0]['InstanceStatus']['Status']

    if instance_status == 'ok':
        LOGGER.info('Aborts. EC2 Status is ok')
        return
    else:
        LOGGER.info('EC2 status is not ok')

def lambda_handler(event, context):
    # TODO implement
    
    try:
        ec2_status()
    except Exception as error:
        LOGGER.exception(error)
    return 'Complete'
