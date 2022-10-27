
from http import client
from venv import create
import boto3
import unittest


client = boto3.client('s3')

def createbucket(name):
    client = boto3.client('s3')
    bucket = client.create_bucket(Bucket = name,CreateBucketConfiguration = {'LocationConstraint':'ap-south-1'})
                
    return bucket['Location']

# print(createbucket('operative-aws-training-1'))



#  There should be a bucket policy created first in order to get it
def check_bucketPolicy(name):
    
    return client.get_bucket_policy(Bucket = name)

print(check_bucketPolicy('operative-aws-training-1'))










