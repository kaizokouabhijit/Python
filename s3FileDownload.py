import unittest
import boto3

def downloadFile():
    s3 = boto3.client('s3')

    bucket = 'operative-aws-trainoing-3'
    key = 'Demo.txt'
    filename= 'DownloadDemo.txt'

    resp = s3.download_file(Bucket = bucket,Key = key, Filename = filename)
    return resp




class fileDownloadTest(unittest.TestCase):

    def test_fileDownload(self):
        result = downloadFile()

        self.assertEqual(result, None)









if __name__ == '__main__':
    unittest.main()