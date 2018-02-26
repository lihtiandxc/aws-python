from datetime import datetime
import boto3
import json
import os

sns_client = boto3.client('sns')

###-------Global Var can be defined in Lambda global var and import with os.environ() method
#str_asg_name = 'limliht-asg,limliht2-asg' #simulate global var in lambda
#global_asg_name = str_asg_name.split(',')

accountpf_sg_list = []
sns_topic_arn = ''

def construct_sns_msg(e):
    
    request_parameters = e['requestParameters']
    group_id = request_parameters['groupId']
    ip_permissions = request_parameters['ipPermissions']
    accesskey_id = e['userIdentity']['accessKeyId']
    username = e['userIdentity']['userName']
    event_name = e['eventName']
    aws_region = e['awsRegion']
    source_ip = e['sourceIPAddress']
    event_id = e['eventID']
    
    str_e = json.dumps(e)
    str_e_data = json.loads(str_e)
    event_time_json = str_e_data['eventTime']
    #Transform the JSON time format to datetime format
    event_time_datetime_format = str(datetime.strptime(event_time_json, '%Y-%m-%dT%H:%M:%SZ'))
    
    rules = json.dumps(ip_permissions['items'])
    
    body_msg = 'Event summary: \
    \n\nEvent name : ' + event_name + \
    '\nSecurity Group ID : ' + group_id + \
    '\nChange Items : ' + json.dumps(rules) + \
    '\nEvent Id : ' + event_id + \
    '\nEvent time (UTC) : ' + event_time_datetime_format + \
    '\nUser Access Key : ' + accesskey_id + \
    '\nUsername : ' + username + \
    '\nAWS Region : ' + aws_region + \
    '\nSource IP : ' + source_ip + \
    '\n\n\n' + 'Raw event: ' + \
    '\n\n' + str_e 
    
    subject_msg = 'Account Platform Security Group ({}) Rules Changes'.format(group_id)
    trigger_notification(body_msg, subject_msg)

def trigger_notification(event_detail, subject):
    
    sns_client.publish(TargetArn = sns_topic_arn, MessageStructure = 'string', \
    Message = event_detail, Subject = subject)

    
def lambda_handler(event, context):
    # TODO implement
    print(event)
    if (event['detail']['eventName'] == 'AuthorizeSecurityGroupIngress' or \
    'AuthorizeSecurityGroupEgress' or 'RevokeSecurityGroupEgress' or\
    'RevokeSecurityGroupIngress') and event['detail']['requestParameters'] \
    ['groupId'] in accountpf_sg_list:
        result = construct_sns_msg(event['detail'])
    
    return 'Success'
