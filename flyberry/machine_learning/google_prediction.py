import argparse
import httplib2
import os
import sys
import json
import time

from apiclient import discovery
from apiclient.discovery import build as discovery_build
from apiclient.errors import HttpError
from apiclient.http import MediaFileUpload
from apiclient.http import MediaIoBaseDownload
from json import dumps as json_dumps
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage as CredentialStorage
from oauth2client.tools import run as run_oauth2
from oauth2client import file
from oauth2client import client
from oauth2client import tools

# Define sample variables.
_BUCKET_NAME = 'flyberry'
_API_VERSION = 'v1'

# Retry transport and file IO errors.
RETRYABLE_ERRORS = (httplib2.HttpLib2Error, IOError)

# Number of times to retry failed downloads.
NUM_RETRIES = 5

# Number of bytes to send/receive in each request.
CHUNKSIZE = 2 * 1024 * 1024

# Mimetype to use if one can't be guessed from the file extension.
DEFAULT_MIMETYPE = 'application/octet-stream'

# Parser for command-line arguments.
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[tools.argparser])


# CLIENT_SECRETS is name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret. You can see the Client ID
# and Client secret on the APIs page in the Cloud Console:
# <https://console.developers.google.com/>
CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')

# File where we will store authentication credentials after acquiring them.
CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), 'credentials.json')

# Set up a Flow object to be used for authentication.
# Add one or more of the following scopes. PLEASE ONLY ADD THE SCOPES YOU
# NEED. For more information on using scopes please see
# <https://developers.google.com/storage/docs/authentication#oauth>.
FLOW = client.flow_from_clientsecrets(CLIENT_SECRETS,
  scope=[
      'https://www.googleapis.com/auth/devstorage.full_control',
      'https://www.googleapis.com/auth/devstorage.read_only',
      'https://www.googleapis.com/auth/devstorage.read_write',
    ],
    message=tools.message_if_missing(CLIENT_SECRETS))
    
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0
To make this sample run you will need to populate the client_secrets.json file
found at:
   %s
with information from the APIs Console
<https://code.google.com/apis/console#access>.
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS))
                                   
class GooglePrediction:
        
    def get_authenticated_service(self):
		storage = file.Storage(CREDENTIALS_FILE)
		credentials = storage.get()
		if credentials is None or credentials.invalid:
		    parser = argparse.ArgumentParser(parents=[tools.argparser])
		    flags = parser.parse_args()
		    credentials = tools.run_flow(FLOW, storage, flags)
		
		
		# Create an httplib2.Http object to handle our HTTP requests and authorize it
		# with our good Credentials.
		http = httplib2.Http()
		http = credentials.authorize(http)
		
		# Construct the service object for the interacting with the Cloud Storage API.
		return discovery.build('storage', _API_VERSION, http=http)
        
    def upload(self, name, directory):
        
        assert name and directory
        filename = name

        now = time.time()
        bucket_name = _BUCKET_NAME
        object_name = name
        
        service = GooglePrediction().get_authenticated_service()
    
        print 'Building upload request...'
        media = MediaFileUpload(filename, chunksize=CHUNKSIZE, resumable=True)
        if not media.mimetype():
            media = MediaFileUpload(filename, DEFAULT_MIMETYPE, resumable=True)
        request = service.objects().insert(bucket=bucket_name, name=object_name,
                                           media_body=media)
    
        print 'Uploading file: %s to bucket: %s object: %s ' % (filename, bucket_name,
                                                                object_name)
    
        progressless_iters = 0
        response = None
        while response is None:
            error = None
            try:
                progress, response = request.next_chunk()
                if progress:
                  print_with_carriage_return('Upload %d%%' % (100 * progress.progress()))
            except HttpError, err:
                error = err
                if err.resp.status < 500:
                  raise
            except RETRYABLE_ERRORS, err:
                error = err
        
            if error:
                progressless_iters += 1
                handle_progressless_iter(error, progressless_iters)
            else:
                progressless_iters = 0
    
        print '\nUpload complete!'
    
        print 'Uploaded Object:'
        print json_dumps(response, indent=2)        
    
    def train(self, data, model_name):
        print "train1"

    def predict(self, model, sample):
        print "predict1"
