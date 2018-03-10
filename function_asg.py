import boto3

asg_client = boto3.client('autoscaling')


autoscaling_group = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=['limliht-asg'])
tagging_key = autoscaling_group['AutoScalingGroups'][0]['Tags']
print(tagging_key)
