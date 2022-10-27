import unittest
from urllib import response
from moto import mock_s3
import boto3

def listBuckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    return response['ResponseMetadata']['HTTPStatusCode']
        
# print(listBuckets())

# bucket_name = 'operative-aws-trainoing-3'
def createBucket(bucket_name):
    s3 = boto3.client('s3')
    bucket = s3.create_bucket(Bucket = bucket_name,CreateBucketConfiguration={'LocationConstraint':'us-west-1'})

    return(bucket['ResponseMetadata']['HTTPStatusCode'])

# createBucket(bucket_name)


def fileupload():
    res = boto3.resource('s3')
    createBucket('operative-aws-trainoing-3')

    response = res.Bucket('operative-aws-trainoing-3').upload_file('Demo.txt', 'Demo.txt')
    return response






class MyTest(unittest.TestCase):
    mock_s3 = mock_s3()
    bucket_name = 'operative-aws-trainoing-3'
    content = 200
    def setUp(self):
        self.mock_s3.start()

        
        s3 = boto3.client('s3')
        

    def tearDown(self):
        self.mock_s3.stop()

    def test_listbucket(self):
        #These are the list of buckets in My AWS S3 right now
        
        

        
        response =listBuckets()

        
       
        
        Bucket_list = self.s3.list_buckets()   # Bucket_list should be a list, but gives some weird value 
        self.assertEqual(Bucket_list['ResponseMetadata']['HTTPStatusCode'], self.content)
    
    def test_createbucket(self):

        createBucket(self.bucket_name)

        s3 = boto3.client('s3')
        testbucket = "Testbucket"
        response = s3.create_bucket(Bucket = testbucket, CreateBucketConfiguration={'LocationConstraint':'us-west-1'})
        self.assertEqual(response['ResponseMetadata']['HTTPStatusCode'], self.content)

    def test_fileupload(self):
        fileupload()
        s3 = boto3.client('s3')
        name = 'testBucket'
        res = boto3.resource('s3')
        s3.create_bucket(Bucket = name,CreateBucketConfiguration={'LocationConstraint':'us-west-1'})

        response = res.Bucket(name).upload_file('Demo.txt', 'Demo.txt')

        self.assertEqual(response, None)

        

        



if __name__ == '__main__':
    unittest.main()