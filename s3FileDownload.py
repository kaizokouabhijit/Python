import boto3

def downloadFile():
    s3 = boto3.resource('s3')

    bucket = 'operative-aws-trainoing-3'
    key = 'Demo.txt'
    Filename= 'DownloadedDemo.txt'

    s3.meta.client.download_file(bucket, key, Filename)


