import boto3

s3 = boto3.client('s3')
bucket = 'operative-aws-trainoing-3'
key = 'Demo.txt'

response = s3.head_object(Bucket = bucket, Key = key)


#response['ResponseMetadata']['forOnTargetTraining'] = True


