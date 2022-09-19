import logging
from venv import create
import boto3
from botocore.exceptions import ClientError


import boto3

client = boto3.client('s3')



# Listing the buckets
bucket_list = client.list_buckets()

for bucket in bucket_list['Buckets']:
    print(bucket['Name'])

#creating buckets
def createbucket(name):
    bucket = client.create_bucket(Bucket = name,
                CreateBucketConfiguration={'LocationConstraint':'us-west-1'})
    print(bucket)



# createbucket('operative-aws-trainoing-3')


