import boto3


# AWS S3 Bucker controller
class Bucket:

    def __init__(self, bucket='autograders', backup_bucket='autograders-backup'):
        self.name = bucket
        self.backup_name = backup_bucket
        self.resource = boto3.resource('s3')
        self.client = boto3.client('s3')
        self.bucket = self.resource.Bucket(bucket)
        self.backup_bucket = self.resource.Bucket(self.backup_name)

    # downloads a key to a specified location (to)
    def download(self, key, to):
        self.bucket.download_file(key, to)

    # downloads a key from backup bucket to a specified location (to)
    def download_backup(self, key, to):
        self.backup_bucket.download_file(key, to)

    # deletes a file from bucket
    def delete(self, key):
        self.client.delete_object(Bucket=self.name, Key=key)

    # creates a backup of a key
    def backup(self, key):
        self.client.copy(CopySource={'Bucket': self.name, 'Key': key}, Bucket=self.backup_name, Key=key)

    # lists all files in bucket
    def list(self):
        return self.bucket.objects.all()
