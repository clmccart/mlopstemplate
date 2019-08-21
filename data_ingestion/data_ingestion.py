# data from blob (or whatever) to dataframe 
# covered by integration tests
import os
import string
from azure.storage.blob import BlockBlobService
import json

with open('secrets.json') as json_file:
    secrets = json.load(json_file)
blob_secrets = secrets['blob']

block_blob_service = BlockBlobService(account_name=blob_secrets['account_name'], account_key=blob_secrets['account_key'])
container_name = 'data'
local_path = './'
local_file_name = 'temp_iris.csv'


# List the blobs in the container.
print("\nList blobs in the container")
generator = block_blob_service.list_blobs(container_name)
for blob in generator:
    print("\t Blob name: " + blob.name)


# Download the blob(s).
full_path_to_file2 = os.path.join(local_path)
print("\nDownloading blob to " + full_path_to_file2)
block_blob_service.get_blob_to_path(container_name, local_file_name, full_path_to_file2)
