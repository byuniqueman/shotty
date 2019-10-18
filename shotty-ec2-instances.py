#!/usr/local/bin/python3

import boto3
import click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

@click.command() # hand off function to click
def list_instances():
    "List EC2 instances" # docstring
    for i in ec2.instances.all():
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)))
            
    # instance attributes
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#instance
    
    return
    
if __name__ == '__main__':
    list_instances()
    
    
    

