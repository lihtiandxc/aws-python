import boto3
import json
import datetime

now = datetime.datetime.now()
s3res = boto3.resource('s3')
ec2client = boto3.client('ec2')
current_month = str(now.month)
current_day = str(now.day)
aws_region = 'us-east-1'


def get_account_ec2_list():
    construct_ec2_list = []
    all_account_ec2 = ec2client.describe_instances(Filters=[{'Name':'tag:Service','Values':['account']},{'Name':'tag:Env','Values':['production']}])
    list_account_ec2 = all_account_ec2['Reservations']
    for each_account_ec2 in list_account_ec2:
        account_ec2 = each_account_ec2['Instances']
        for each_account_ec2_id in account_ec2:
            ec2_id = each_account_ec2_id['InstanceId']
            #ec2_tag = each_account_ec2_id['Tags']
            #print(ec2_id)
            #print(ec2_tag)
            construct_ec2_list.append(ec2_id)
    print(construct_ec2_list)
    return construct_ec2_list

def put_list_to_s3(r):
    #print(r)
    obj = s3res.Object('limliht-config','config/'+aws_region+'/'+current_month+'/'+current_day+'/default_document.json')
    obj.put(Body=json.dumps(r))

#read file from s3

#read_data = obj.get()['Body'].read()
#print(read_data)

if __name__ == "__main__":
    try:
        result = get_account_ec2_list()
        put_list_to_s3(result)
        print('done')
    except:
        print('error')
