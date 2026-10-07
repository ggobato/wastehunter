import boto3

ec2 = boto3.client('ec2')

def describe_volumes():

    response = ec2.describe_volumes(
        Filters=[
            {
                'Name': 'status',
                'Values': [
                    'available'
                ]
            }
        ]
    )

    for volumes in response:

        unattached_vol = []
        
        volumes = response["Volumes"][0]["VolumeId"]
        unattached_vol.append(volumes)

    return unattached_vol

