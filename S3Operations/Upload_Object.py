
import boto3


def file_upload(filename):
    resource = boto3.resource('s3')
    response = resource.Bucket('operative-aws-training-1').upload_file(filename, "Demo.txt")
    return response



print(file_upload('Demo.txt'))