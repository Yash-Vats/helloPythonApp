"""
This script runs the FlaskTemplate application using a development server.
"""
import os

app.config['BLOB_ACCOUNT'] = os.getenv("BLOB_ACCOUNT")
app.config['BLOB_STORAGE_KEY'] = os.getenv("BLOB_STORAGE_KEY")
app.config['BLOB_CONTAINER'] = os.getenv("BLOB_CONTAINER")

from os import environ
from FlaskTemplate import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '3000'))
    except ValueError:
        PORT = 3000
    app.run(HOST, PORT)

from azure.storage.blob import BlobServiceClient

blob_container = app.config['BLOB_CONTAINER']

storage_url = "https://{}.blob.core.windows.net/".format(
    app.config['BLOB_ACCOUNT']
)

blob_service = BlobServiceClient(
    account_url=storage_url,
    credential=app.config['BLOB_STORAGE_KEY']
)

blob_client = blob_service.get_blob_client(
    container=blob_container,
    blob=filename
)

blob_client.upload_blob(file)
