import json
import logging
import os

from google.oauth2 import service_account
from google.cloud import storage
from google.cloud.exceptions import NotFound

class GcpService:
    """A class to handle interactions with the GCP services."""

    def __init__(self):
        """Establish connection information."""

        self.credentials_path = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS_JSON_PATH')
        if self.credentials_path:
            with open(self.credentials_path) as json_file:
                self.credentials = json.load(json_file)
                self.creds = service_account.Credentials.from_service_account_info(self.credentials)
        else:
            raise ValueError('GCP Service credentials are not configured.')

    def _get_storage_client(self):
        """Get storage client with credentials."""
        project_id = self.credentials.get('project_id')
        return storage.Client(project=project_id, credentials=self.creds)

    def create_storage_bucket(self, bucket_name):
        """Create storage bucket in given region.

        Buckets are created in the us multi-regional location
        and have a default storage class of Standard Storage.

        Note: In order to create a bucket in a project, a user
        must have the storage.objects.create project permission
        for the project. If you are working within a project that
        you did not create, you might need the project owner to
        give you a role that contains this permission, such as
        Editor, Owner, or Storage Admin.
        
        :param bucket_name: The name of the storage bucket
        :return: True if bucket is created, else False
        """
        try:
            storage_client = self._get_storage_client()
            storage_client.create_bucket(bucket_name)
        except Exception as e:
            logging.error(e)
            return False
        return True

    def get_storage_bucket(self, bucket_name):
        """Retrieves the storage bucket by name.

        :param bucket_name: The name of the storage bucket to retrieve
        :return: The storage bucket or None
        :return: An iterator of blobs or None
        """
        bucket = None
        blobs = None
        storage_client = self._get_storage_client()
        bucket = storage_client.lookup_bucket(bucket_name)
        if bucket:
            blobs = storage_client.list_blobs(bucket_name)
        return bucket, blobs

    def delete_storage_bucket(self, bucket_name):
        """Delete the storage bucket by name.

        :param bucket_name: The name of the storage bucket
        :return: True if bucket is deleted, else False
        """
        try:
            storage_client = self._get_storage_client()
            bucket = storage_client.lookup_bucket(bucket_name)
            if bucket:
                bucket.delete()
            else:
                False
        except Exception as e:
            logging.error(e)
            return False
        return True