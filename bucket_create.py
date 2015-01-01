#!/usr.bin/python

import boto
import gcs_oauth2_boto_plugin
import os
import shutil
import StringIO
import tempfile
import time

GOOGLE_STORAGE = 'gs'
LOCAL_FILE = 'file'

CLIENT_ID = '890531800530-dbt68a393gn72rt08vnkke3vf374phtf.apps.googleusercontent.com'
CLIENT_SECRET = 'sJpFPNCKqYQRFvU9UDx3y1K7'
gcs_oauth2_boto_plugin.SetFallbackClientIdAndSecret(CLIENT_ID, CLIENT_SECRET)

now = time.time()

CATS_BUCKET = 'cats-%d' % now
DOGS_BUCKET = 'dogs-%d' % now

project_id = 'foxdie-service'

for name in (CATS_BUCKET, DOGS_BUCKET):
    uri = boto.storage_uri(name, GOOGLE_STORAGE)
    try:
        header_values = {"x-goog-project-id": project_id}
        uri.create_bucket(headers=header_values)

        print 'Successfully created bucket "%s"' % name
    except Exception, e:
        print 'Failed to create bucket. %s' % e
    
    
uri = boto.storage_uri('', GOOGLE_STORAGE)
# If the default project is defined, call get_all_buckets() without arguments.
for bucket in uri.get_all_buckets(headers=header_values):
  print bucket.name    