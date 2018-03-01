#!/usr/bin/python

import os,sys
import boto3
import argparse
import time
import operator

def print_priv_dns(instances, ec2):

    for i in instances:
        print(ec2.Instance(i).private_dns_name.replace('.ec2.internal', ''))

def get_asg_from_stack(stack_name, client):

    asg = list()

    stk_response = client.describe_stack_resources(StackName=stack_name)

    for resp in stk_response['StackResources']:
        for resrc_type in resp:
            if resrc_type == "ResourceType":
                if resp[resrc_type] == "AWS::AutoScaling::AutoScalingGroup":
                    asg.append(resp['PhysicalResourceId'])

    return asg

def get_inst_from_asg(asg, client_asg, ec2 ):

    response = client_asg.describe_auto_scaling_groups(AutoScalingGroupNames=[asg])

    instances = list()
    # Build instance IDs list
    for r in response['AutoScalingGroups']:
        for i in r['Instances']:
            instances.append(ec2.Instance(i['InstanceId']).instance_id)

    return instances


def main():

    region = "Ref('AWS::Region')"
    stack_name = "Ref('AWS::StackName')"
    instances = list()

    asg_client = boto3.client('autoscaling', region_name=region)
    ec2 = boto3.resource('ec2', region_name=region)
    cfn_client = boto3.client('cloudformation', region_name=region)

    asg_list = get_asg_from_stack(stack_name, cfn_client)

    for asg in asg_list:
        for i in get_inst_from_asg(asg, asg_client, ec2):
            instances.append(i)

    print_priv_dns(instances, ec2)



if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print 'Received Keyboard interrupt.'
        print 'Exiting...'