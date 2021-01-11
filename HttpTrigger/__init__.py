import logging

import azure.functions as func
from azure.storage.blob import BlobServiceClient
import json
import os 
import pymongo
import datetime


def main(req: func.HttpRequest, outputQueueItem: func.Out[func.QueueMessage]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Blob Storage- Upload

    conn_str = f'DefaultEndpointsProtocol=https;AccountName=azurestorageacc86;AccountKey=11IZkcgITC4oqNdUo8s82C9/xl49ugXJA97XsXgmDyYaaDNs76ucNr8elfk1HzCUv9nxCtXVSv39rZZuF8W7Ug==;EndpointSuffix=core.windows.net'
    blob_service_client = BlobServiceClient.from_connection_string(
        conn_str=conn_str)
    logging.info(os.path.abspath)
    '''blob_client = blob_service_client.get_blob_client(container='imagecon', blob='pic.png')
    with open(os.path.abspath('file.png'), 'rb') as my_blob:
        blob_client.upload_blob(my_blob,overwrite=True)
        blob_client.close()'''


    # Blob Storage- Download
    blob_client = blob_service_client.get_blob_client(container='imagecon', blob='index.png')
    with open('index.png', 'wb') as my_blob:
        my_blob.writelines([blob_client.download_blob().readall()])
        my_blob.close()


    # Cosmos DB

    '''uri = "mongodb://azurecosmosdbacc86:LbZMRoslYgqLVQ3WuaDXRyLFJ7IncY0uLHjUPmNS5VoOVvK9V5wBgkMJIIROsJWEIwCOnS6qJssmGm7bs57yxA==@azurecosmosdbacc86.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@azurecosmosdbacc86@"
    client = pymongo.MongoClient(uri, retryWrites=False)
    db = client['demodb']
    collection = db['con1']
    record = {
        "author": "Joe",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
    }
    id = collection.insert_one(record)
    logging.info(f'Created ID {id}')'''

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        ob = {'enteredName':name}
        # Set message in the queue storage for logging purpose.
        # outputQueueItem.set(name)
        return func.HttpResponse(json.dumps(ob))
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
