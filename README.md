# gcp-cost-mgmt-access
Proof of concept code to setup an cost mgmt data extraction and pull data file. 

## Background
The sample code here is meant to setup Billing export to a file as described in this [Google Cloud Platform (GCP) document](https://cloud.google.com/billing/docs/how-to/export-data-file) and provide code to extract and read the report data once downloaded.

## Getting Started

1. Clone the repository:
```
git clone https://github.com/chambridge/gcp-cost-mgmt-access.git
```

2. Setup virtual environment with _pipenv_
```
cd gcp-cost-mgmt-access
pipenv install
```

3. Create a service account
Follow the steps in the following GCP document to [create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts)

Add the following roles to the service account: _Storage Admin_, _Role2_, and _Role3_.


4. Set environment variables
Copy the `.env.example` file to `.env` and provide the necessary variables.
```
cp ./.env.example ./.env
```

5. Enter virtual environment shell with set environment variables
```
pipenv shell
```

## Code Structure

Currently, the code to interact with GCP resides in the `cloud` directory. Outside of this there are several single purpose scripts to work with storage buckets billing export. These scripts can be called directedly as seen in the following example:

```
python setup_storage_bucket.py
```