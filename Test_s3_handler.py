from s3DownloadMoto import Handler
from moto import mock_s3
import boto3



@mock_s3
def test():

    s3_client = boto3.client('s3')
    s3DownloadMoto = Handler()

    s3DownloadMoto.download_s3_file()