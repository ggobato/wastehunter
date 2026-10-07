import boto3
import json
from checks import ebs_unattached

def lambda_handler(event, context):
    
    response = ebs_unattached.describe_volumes()

    return response

