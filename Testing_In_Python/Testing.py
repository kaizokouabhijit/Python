import json
import urllib.parse
import boto3
import os
import logging

from moto import mock_s3

log = logging.getLogger()
log.setLevel(logging.INFO)

import unittest





print('Loading function')

# f = open("C:\Users\abhijit.s\OneDrive - SintecMedia Ltd\Desktop\git\PythonEvents.json")
# event = json.load(f)
# f.close()

s3 = boto3.client('s3')
s3_res = boto3.resource('s3')


def lambda_handler(event, context = None):
    # print("Received event: " + json.dumps(event, indent=2))

    # log.info("Log info")
    # log.info(os.environ['AWS_LAMBDA_LOG_GROUP_NAME'])
    # log.info(event)

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    
    obj = s3_res.Object(bucket, key)
    data = obj.get()['Body'].read()

    # bucket_list = s3.list_buckets()
    # dest_bucket = bucket_list['Buckets'][2]['Name']

    # dest_bucket = os.environ['DEST_BUCKET']
    dest_bucket = 'operative-aws-training2'

    write_data = b'data'
    object = s3_res.Bucket(dest_bucket).Object(key)
    res = object.put(Body=write_data)

    log.info("Status code of the response")

    return res['ResponseMetadata']['HTTPStatusCode']




# lambda_handler(event, context=None)



class test(unittest.TestCase):
    mock_s3 = mock_s3()

    

    content = 200

    def setUp(self):
        self.mock_s3.start()

        s3 = boto3.client('s3')

    def tearDown(self):
        self.mock_s3.stop()

    def test_handle(self):
        


        lambda_handler(event, context = None)

        dest_bucket = 'operative-aws-training2'
        keyname = 'document1-1.docx'
        s3_res = boto3.resource('s3')
        obj = s3_res.Object(dest_bucket, keyname)
        data = obj.get()['Body'].read()
        self.assertIsNotNone(data)
































