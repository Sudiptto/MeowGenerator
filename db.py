import os
from azure.cosmos import CosmosClient, exceptions, PartitionKey
import json 
import asyncio
from passwords import *

url = COSMOS_ENDPOINT
key = COSMOS_KEY

#create Cosmos Client 
client = CosmosClient(url, credential=key)
DATABASE_NAME = 'MeowGenerator'
database= client.get_database_client(DATABASE_NAME) 
CONTAINER_NAME = 'Stories'
container = database.get_container_client(CONTAINER_NAME)


# returns information of all fields that exist in db
def get_data():
    str = None
    for item in container.query_items(query=f'SELECT * FROM mycontainer s',enable_cross_partition_query=True):
        str = json.dumps(item,indent=True)
    return str


# check if any data exists within the database
def data_exists():
    item = get_data()
    if item is not None:
        return True
    return False



# Function to update an existing field
#@param jfile: updated json data that needs to be sent to the cloud
def update_json(jfile):
    # if db is empty, then add an entry with given json file
    if not data_exists():
        container.upsert_item({
            'id': '1',
            'partition_key': '1',
            'stories': jfile,
        })
        return
    
    #if there is already json data for any stories, then update it by replacing the field
    # Query the document by id
    query = f'SELECT * FROM mycontainer c"'
    for item in container.query_items(query=query, enable_cross_partition_query=True):
        # Update the specific field
        item["stories"] = jfile

        # Replace the document with the updated one
        container.replace_item(item=item['id'], body=item)
        print(f"Document has been updated.")

def clear():
    for item in container.query_items(query='SELECT * FROM mycontainer s',enable_cross_partition_query=True):
            container.delete_item(item, partition_key=item['id'])