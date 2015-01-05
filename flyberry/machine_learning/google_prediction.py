import argparse
import httplib2
import os
import sys
import json
import time
import urllib
import urllib2
import pprint

from apiclient import discovery
from apiclient.discovery import build as discovery_build
from apiclient.errors import HttpError
from apiclient.http import MediaFileUpload
from apiclient.http import MediaInMemoryUpload
from apiclient.http import MediaIoBaseDownload
from json import dumps as json_dumps
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage as CredentialStorage
from oauth2client.tools import run as run_oauth2
from oauth2client import file
from oauth2client import client
from oauth2client import tools

# Define sample variables.
_BUCKET_NAME            = 'flyberry'
_API_VERSION            = 'v1'
_PREDICTION_API_VERSION = 'v1.6'
_PROJECT                = 'foxdie-service'
_PROJECT_NUMBER         = '890531800530'

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
      'https://www.googleapis.com/auth/prediction',
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
    
    @staticmethod
    def get_credentials():
        storage = CredentialStorage(CREDENTIALS_FILE)
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            parser = argparse.ArgumentParser(parents=[tools.argparser])
            flags = parser.parse_args()
            credentials = tools.run_flow(FLOW, storage, flags)
        return credentials
		
    @staticmethod
    def get_authenticated_service():
		
		credentials = GooglePrediction.get_credentials()
		# Create an httplib2.Http object to handle our HTTP requests and authorize it
		# with our good Credentials.
		http = httplib2.Http()
		http = credentials.authorize(http)
		
		# Construct the service object for the interacting with the Cloud Storage API.
		return discovery.build('storage', _API_VERSION, http=http)
		
    @staticmethod
    def get_predication_service():
        credentials = GooglePrediction.get_credentials()
        # Create an httplib2.Http object to handle our HTTP requests and authorize it
        # with our good Credentials.
        http = httplib2.Http()
        http = credentials.authorize(http)
        
        # Construct the service object for the interacting with the Cloud Storage API.
        return discovery.build('prediction', _PREDICTION_API_VERSION, http=http)
    
    def upload(self, name, directory):
        
        assert name and directory
        filename = name
        
        now = time.time()
        bucket_name = _BUCKET_NAME
        object_name = name
        
        service = GooglePrediction.get_authenticated_service()
        
        print 'Building upload request...'
        if directory.startswith('http'):
            url = directory
            req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
            response = urllib2.urlopen(req)
            the_page = response.read()
            media = MediaInMemoryUpload(the_page, 'text/plain', chunksize=CHUNKSIZE, resumable=True)
        else:
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
        print 'start to train...'
        # Get access to the Prediction API.
        service = GooglePrediction.get_predication_service()
        papi = service.trainedmodels()
        # Start training request on a data set.
        print 'Submitting model training request'
        body = {'project': _PROJECT,'id': model_name, 'storageDataLocation': data}
        start = papi.insert(project=_PROJECT, body=body).execute()
        print 'Training results:'
        pprint.pprint(start)
        
    def predict(self, model, sample):
        if not isinstance(sample, (list, tuple)):
            input_data = [sample]
        else:
            if isinstance(sample, list):
                for item in sample:
                    input_data = item
                    body = {'input': {'csvInstance': input_data}}
                    result = GooglePrediction.get_predication_service().trainedmodels().predict(
                        fields = 'outputLabel,outputValue',
                        project = _PROJECT_NUMBER, id=model, body=body).execute()
                    print result
            else:
                input_data = sample
                body = {'input': {'csvInstance': input_data}}
                return GooglePrediction.get_predication_service().trainedmodels().predict(
        			project = _PROJECT_NUMBER,
        			id=model,
        			body=body).execute()
		
    def list(self, model):
        service = GooglePrediction.get_predication_service()
        papi = service.trainedmodels()
        
        # List models.
        print_header('Fetching list of first ten models')
        result = papi.list(project=_PROJECT, maxResults=10).execute()
        print 'List results:'
        pprint.pprint(result)
        
    def get(self, model):
        service = GooglePrediction.get_predication_service()
        papi = service.trainedmodels()
        print_header('Get model.')
        result = papi.get(project=_PROJECT, id=model).execute()
        print 'Get results:'
        pprint.pprint(result)
        
def print_with_carriage_return(s):
    sys.stdout.write('\r' + s)
    sys.stdout.flush()

def print_header(line):
    '''Format and print header block sized to length of line'''
    header_str = '='
    header_line = header_str * len(line)
    print '\n' + header_line
    print line
    print header_line