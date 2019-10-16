import json
import boto3
from pprint import pprint

def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('ec2', region_name='ap-southeast-2')
    response = client.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [
                    'running'
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
    stop_list = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # pprint("Stopping Instance with id : " + instance['InstanceId'])
            stop_list.append(instance['InstanceId'])
    try:
        response = client.stop_instances(InstanceIds=stop_list)
        pprint(response['ResponseMetadata']['HTTPStatusCode'])
        pprint(response['StoppingInstances'])
    except botocore.exceptions.ClientError:
        print("The last API call errored out. Information below !!!")
        print("ERROR:", sys.exc_info())
    except:
        print("Unknown Error : ", sys.exc_info())

    return {
        'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
        # 'body': json.dumps('Hello from Lambda!')
        'body': response['StoppingInstances']
    }

