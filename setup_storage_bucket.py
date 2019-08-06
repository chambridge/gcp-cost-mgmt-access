import os

from cloud.gcp_service import GcpService

def main():
    """Execute script."""
    storage_bucket = os.environ.get(
        'STORAGE_BUCKET', 'costmgmtacct1234')
    gcp = GcpService()
    result = gcp.create_storage_bucket(storage_bucket)
    if result:
        print(f'Storage bucket {storage_bucket} was created.')
    else:
        print(f'Failed to create storage bucket {storage_bucket}.')

main()