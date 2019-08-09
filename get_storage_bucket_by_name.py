import os

from cloud.gcp_service import GcpService

def main():
    """Execute script."""
    storage_bucket = os.environ.get(
        'STORAGE_BUCKET', 'costmgmtacct1234')
    gcp = GcpService()
    bucket = gcp.get_storage_bucket(storage_bucket)

    if bucket:
        print(f'{storage_bucket}={bucket}')
    else:
        print(f'Failed to retrieve storage bucket {storage_bucket}.')


main()