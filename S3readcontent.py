import boto3

Bucket_read = 'operative-aws-training-2'

ObjectFile = 'awskeys.txt'


def read_file(Bucket_read, ObjectFile):
    s3 = boto3.resource('s3')
    """ :type : pyboto3.s3 """

    obj = s3.Bucket(Bucket_read).Object(ObjectFile).get()
    print(obj['Body'])

    return(obj['Body'].read().decode())


content = read_file(Bucket_read, ObjectFile)

Bucket_write = 'operative-aws-s3transactionstore'
KeyFile = 'awskeys.txt'


def Write_file(Bucket_write, KeyFile, content):
    data = b'content'
    s3 = boto3.resource('s3')
    object = s3.Bucket(Bucket_write).Object(KeyFile)
    res = object.put(Body = data)
    print(res['ResponseMetadata']['HTTPStatusCode'])



Write_file(Bucket_write, KeyFile, content)
