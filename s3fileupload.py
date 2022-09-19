import boto3

s3 = boto3.resource('s3')

bucket_name = 'operative-aws-trainoing-3'
response = s3.Bucket(bucket_name).upload_file('Demo.txt', 'Demo.txt')

print(response)


