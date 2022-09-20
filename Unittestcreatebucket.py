import unittest
import logging
from venv import create
import boto3



import boto3

client = boto3.client('s3')

def createbucket(name):
    bucket = client.create_bucket(Bucket = name,CreateBucketConfiguration={'LocationConstraint':'us-west-1'})
                
    print(bucket['Location'])



createbucket('operative-aws-trainoing-3')

class UnittestDemo(unittest.TestCase):
    def test_createbucket(self):
        name = 'operative-aws-trainoing-3'


        result = createbucket(name)
        self.assertEqual(result, 'http://operative-aws-trainoing-3.s3.amazonaws.com/')


if __name__ == "__main__":
    unittest.main()
