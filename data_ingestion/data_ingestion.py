# data from blob (or whatever) to dataframe 
# covered by integration tests
import os
import string
from azure.storage.blob import BlockBlobService
import json    
from io import StringIO
import pandas as pd

with open('secrets.json') as json_file:
    secrets = json.load(json_file)
blob_secrets = secrets['blob']

block_blob_service = BlockBlobService(account_name=blob_secrets['account_name'], account_key=blob_secrets['account_key'])
container_name = blob_secrets['container_name']



# List the blobs in the container.
print("\nList blobs in the container")
generator = block_blob_service.list_blobs(container_name)
for blob in generator:
    print("\t Blob name: " + blob.name)
    blobstring = block_blob_service.get_blob_to_text(container_name, blob.name).content
    df = pd.read_csv(StringIO(blobstring))
    print(df.head())


