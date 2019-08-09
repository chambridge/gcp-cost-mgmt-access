import csv
import os

from cloud.gcp_service import GcpService

def main():
    """Execute script."""
    storage_bucket = os.environ.get('STORAGE_BUCKET', 'costmgmtacct1234')
    cost_report = os.environ.get('COST_REPORT', 'creport')
    gcp = GcpService()
    file_path = gcp.download_latest_cost_report(storage_bucket, cost_report)

    print(f'file_path={file_path}')
    
    with open(file_path) as csv_file:
        read_csv = csv.reader(csv_file, delimiter=',')
        print('First 3 rows.')
        row_count = 0
        for row in read_csv:
            print(row)
            row_count = row_count + 1
            if row_count >= 3:
                break


main()