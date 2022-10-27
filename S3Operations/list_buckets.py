import boto3

def list_buckets():
    client = boto3.client('s3')

    bucket_list = client.list_buckets()

    for bucket in bucket_list['Buckets']:
        print(bucket['Name'])


list_buckets()