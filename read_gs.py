#!/usr/bin/python

from boto import storage_uri
from gcs_oauth2_boto_plugin import oauth2_plugin
content = storage_uri('gs://flyberry/language_id.txt').get_contents_as_string()
print(content)
