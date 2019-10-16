import json
import boto3
import botocore
import sys
from pprint import pprint

def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('ec2', region_name='ap-southeast-2')
    response = client.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [
                    'stopped'
                ]
            },
            {
                'Name': 'tag:nightOff',
                'Values': [
                    'yes'
                ]
            },
        ]
    )
    start_list = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            start_list.append(instance['InstanceId'])
    try:
        response = client.start_instances(InstanceIds=start_list)
        pprint(response['ResponseMetadata']['HTTPStatusCode'])
        pprint(response['StartingInstances'])
        return {
            'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
            'body': response['StartingInstances']
        }
    except botocore.exceptions.ClientError:
        print("The last API call errored out. Information below !!!")
        print("NO ACTION TAKEN:", sys.exc_info())
    except:
        print("Unknown Error : ", sys.exc_info())
