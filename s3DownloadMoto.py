import boto3

class Handler:
    def __init__(self) -> None:
        self.s3_session = boto3.session.Session()
        self.s3_client = self.s3_session.client('s3')
        self.bucket = "My bucket"
        self.filename = 'Demo.txt'
        self.dwnfile = 'DownloadDemo.txt'
        

        def download_s3_file(self):
            self.s3_client.upload_file(
                self.bucket,
                self.filename,
                self.dwnfile
                
            )