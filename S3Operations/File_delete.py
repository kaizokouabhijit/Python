from contextlib import nullcontext
import boto3


client = boto3.client('s3')

def delete_files():
    resource = boto3.resource('s3')
    bucket = resource.Bucket('operative-aws-training-1')

    response = bucket.delete_objects(Delete={
        'Objects': [
            {
                'Key': 'Demo.txt',
                'VersionId': 'null'
            }
        ]
        
    })

    print(response)


delete_files()