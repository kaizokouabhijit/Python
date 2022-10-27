from urllib import response
import boto3

def delete_bucket(name):
    s3 = boto3.client('s3')

    response = s3.delete_bucket(Bucket = name)

    return response['ResponseMetadata']['HTTPStatusCode']

print(delete_bucket('operative-aws-training-1'))

    