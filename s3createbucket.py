
from venv import create
import boto3
import unittest




client = boto3.client('s3')



# Listing the buckets
bucket_list = client.list_buckets()

for bucket in bucket_list['Buckets']:
    print(bucket['Name'])

#creating buckets
def createbucket(name):
    bucket = client.create_bucket(Bucket = name,CreateBucketConfiguration={'LocationConstraint':'us-west-1'})
                
    return bucket['Location']




class testcreatebucket(unittest.TestCase):
    def test_createbucket(self):
        name = 'operative-aws-trainoing-3'

        Location = 'http://operative-aws-trainoing-3.s3.amazonaws.com/'

        res = createbucket(name)
        self.assertEqual(res,Location)
















if __name__ == '__main__':
    unittest.main()
        




