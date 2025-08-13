from google.cloud import storage

class GCSConnector:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.client = storage.Client()

    def list_files(self, prefix=None):
        bucket = self.client.bucket(self.bucket_name)
        blobs = bucket.list_blobs(prefix=prefix)
        return [f"gs://{self.bucket_name}/{blob.name}" for blob in blobs]
