import unittest
from moto import mock_s3
import boto3

def func_to_test():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    return response['ResponseMetadata']['HTTPStatusCode']
        
# print(func_to_test())



class MyTest(unittest.TestCase):
    mock_s3 = mock_s3()
    bucket_name = 'operative-aws-trainoing-3'
    def setUp(self):
        self.mock_s3.start()

        
        s3 = boto3.client('s3')
        

    def tearDown(self):
        self.mock_s3.stop()

    def test(self):
        #These are the list of buckets in My AWS S3 right now
        content = 200
        

        
        func_to_test()

        
        s3 = boto3.client('s3')
        
        Bucket_list = s3.list_buckets()   # Bucket_list should be a list, but gives some weird value 
        self.assertEqual(Bucket_list['ResponseMetadata']['HTTPStatusCode'], content)

        



if __name__ == '__main__':
    unittest.main()