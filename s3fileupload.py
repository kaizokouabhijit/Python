import boto3
import unittest

s3 = boto3.resource('s3')



name = 'Demo.txt'
def uploadfile(name):
    bucket_name = 'operative-aws-trainoing-3'

    response = s3.Bucket(bucket_name).upload_file('Demo.txt', 'Demo.txt')

    return response




class fileuploadTest(unittest.TestCase):
    def test_fileupload(self):
        FileName = 'Demo.txt'

        result = uploadfile(FileName)

        self.assertEqual(result, None)







if __name__ == '__main__':
        unittest.main()

