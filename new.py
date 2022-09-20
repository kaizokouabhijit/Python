import unittest
import boto3
from moto import mock_s3


@mock_s3
class TestMockClassLevel(unittest.TestCase):
    def setUp(self):
        s3 = boto3.client("s3", region_name="us-east-1")
        s3.create_bucket(Bucket="mybucket")

    def test_creating_a_bucket(self):
       

        s3 = boto3.client("s3", region_name="us-east-1")
        s3.create_bucket(Bucket="bucket_inside")