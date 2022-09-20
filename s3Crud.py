import boto3

class s3crud:
    def __init__(self):
        self.s3_session = boto3.session.Session()
        self.s3_client = self.s3_session.client('s3')
        self.bucket = 'my-bucktes'
        self.file_name = "Demo.txt"
        self.file_path = "Demo.txt"

    
    def create_bucket(self):
        bucket = self.s3_client.create_bucket(Bucket = self.bucket, CreateBucketConfiguration={'LocationConstraint':'us-west-1'})


    def upload(self):
        self.s3_client.upload_file(self.file_path, self.bucket, self.file_name)


    create_bucket()
