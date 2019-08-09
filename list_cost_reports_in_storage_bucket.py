import os

from cloud.gcp_service import GcpService

def main():
    """Execute script."""
    storage_bucket = os.environ.get('STORAGE_BUCKET', 'costmgmtacct1234')
    cost_report = os.environ.get('COST_REPORT', 'creport')
    gcp = GcpService()
    blobs = gcp.list_blobs_in_storage_bucket(storage_bucket, cost_report)

    if blobs:
        print(f'Storage Bucket {storage_bucket} blobs:')
        for blob in blobs:
            print(f'blob={blob.name}, {blob.updated}')
    else:
        print(f'Failed to retrieve blobs from storage bucket {storage_bucket}.')


main()