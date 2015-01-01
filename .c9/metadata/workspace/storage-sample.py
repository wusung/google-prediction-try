{"changed":true,"filter":false,"title":"storage-sample.py","tooltip":"/storage-sample.py","value":"# -*- coding: utf-8 -*-\n#\n# Copyright (C) 2013 Google Inc.\n#\n# Licensed under the Apache License, Version 2.0 (the \"License\");\n# you may not use this file except in compliance with the License.\n# You may obtain a copy of the License at\n#\n#      http://www.apache.org/licenses/LICENSE-2.0\n#\n# Unless required by applicable law or agreed to in writing, software\n# distributed under the License is distributed on an \"AS IS\" BASIS,\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n# See the License for the specific language governing permissions and\n# limitations under the License.\n# [START all]\n\"\"\"Command-line skeleton application for Cloud Storage API.\nUsage:\n  $ python storage-sample.py\n\nYou can also get help on all the command-line flags the program understands\nby running:\n\n  $ python storage-sample.py --help\n\n\"\"\"\n\nimport argparse\nimport httplib2\nimport os\nimport sys\nimport json\n\nfrom apiclient import discovery\nfrom oauth2client import file\nfrom oauth2client import client\nfrom oauth2client import tools\n\n# Define sample variables.\n_BUCKET_NAME = 'flyberry'\n_API_VERSION = 'v1'\n\n# Parser for command-line arguments.\nparser = argparse.ArgumentParser(\n    description=__doc__,\n    formatter_class=argparse.RawDescriptionHelpFormatter,\n    parents=[tools.argparser])\n\n\n# CLIENT_SECRETS is name of a file containing the OAuth 2.0 information for this\n# application, including client_id and client_secret. You can see the Client ID\n# and Client secret on the APIs page in the Cloud Console:\n# <https://console.developers.google.com/>\nCLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')\n\n# Set up a Flow object to be used for authentication.\n# Add one or more of the following scopes. PLEASE ONLY ADD THE SCOPES YOU\n# NEED. For more information on using scopes please see\n# <https://developers.google.com/storage/docs/authentication#oauth>.\nFLOW = client.flow_from_clientsecrets(CLIENT_SECRETS,\n  scope=[\n      'https://www.googleapis.com/auth/devstorage.full_control',\n      'https://www.googleapis.com/auth/devstorage.read_only',\n      'https://www.googleapis.com/auth/devstorage.read_write',\n    ],\n    message=tools.message_if_missing(CLIENT_SECRETS))\n\ndef create_bucket(argv):\n  \"\"\"docstring for create_bucket\"\"\"\n  flags = parser.parse_args(argv[1:])\n  storage = file.Storage(\"sample.dat\")\n  credentials = storage.get()\n  if credentials is None or credentials.invalid:\n    credentials = tols.run_flow(FLOW, storage, flags)\n  \n  http = httplib2.Http()\n  http = credentials.authorize(http)\n  \n  service = discovery.build(\"storage\", _API_VERSION, http=http)\n  try:\n    req = \n  except Exception, e:\n    raise e\n\ndef main(argv):\n  # Parse the command-line flags.\n  flags = parser.parse_args(argv[1:])\n\n  # If the credentials don't exist or are invalid run through the native client\n  # flow. The Storage object will ensure that if successful the good\n  # credentials will get written back to the file.\n  storage = file.Storage('sample.dat')\n  credentials = storage.get()\n  if credentials is None or credentials.invalid:\n    credentials = tools.run_flow(FLOW, storage, flags)\n\n  # Create an httplib2.Http object to handle our HTTP requests and authorize it\n  # with our good Credentials.\n  http = httplib2.Http()\n  http = credentials.authorize(http)\n\n  # Construct the service object for the interacting with the Cloud Storage API.\n  service = discovery.build('storage', _API_VERSION, http=http)\n\n  try:\n    req = service.buckets().get(bucket=_BUCKET_NAME)\n    resp = req.execute()\n    print json.dumps(resp, indent=2)\n\n    fields_to_return = 'nextPageToken,items(name,size,contentType,metadata(my-key))'\n    req = service.objects().list(bucket=_BUCKET_NAME, fields=fields_to_return)\n    # If you have too many items to list in one request, list_next() will\n    # automatically handle paging with the pageToken.\n    while req is not None:\n      resp = req.execute()\n      print json.dumps(resp, indent=2)\n      req = service.objects().list_next(req, resp)\n\n  except client.AccessTokenRefreshError:\n    print (\"The credentials have been revoked or expired, please re-run\"\n      \"the application to re-authorize\")\n\nif __name__ == '__main__':\n  main(sys.argv)\n# [END all]","undoManager":{"mark":-45,"position":100,"stack":[[{"group":"doc","deltas":[{"start":{"row":76,"column":23},"end":{"row":76,"column":24},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":24},"end":{"row":76,"column":25},"action":"insert","lines":["h"]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":25},"end":{"row":76,"column":26},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":21},"end":{"row":76,"column":26},"action":"remove","lines":["authe"]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":20},"end":{"row":76,"column":21},"action":"remove","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":20},"end":{"row":76,"column":21},"action":"insert","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":21},"end":{"row":76,"column":22},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":22},"end":{"row":76,"column":23},"action":"insert","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":23},"end":{"row":76,"column":24},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":24},"end":{"row":76,"column":25},"action":"insert","lines":["h"]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":21},"end":{"row":76,"column":25},"action":"remove","lines":["auth"]},{"start":{"row":76,"column":21},"end":{"row":76,"column":30},"action":"insert","lines":["authorize"]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":30},"end":{"row":76,"column":31},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":31},"end":{"row":76,"column":32},"action":"insert","lines":["h"]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":32},"end":{"row":76,"column":33},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":33},"end":{"row":76,"column":34},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":34},"end":{"row":76,"column":35},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":35},"end":{"row":76,"column":36},"action":"insert","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":76,"column":36},"end":{"row":76,"column":37},"action":"remove","lines":[" "]},{"start":{"row":76,"column":36},"end":{"row":77,"column":0},"action":"insert","lines":["",""]},{"start":{"row":77,"column":0},"end":{"row":77,"column":2},"action":"insert","lines":["  "]}]}],[{"group":"doc","deltas":[{"start":{"row":77,"column":0},"end":{"row":77,"column":2},"action":"remove","lines":["  "]}]}],[{"group":"doc","deltas":[{"start":{"row":77,"column":0},"end":{"row":77,"column":2},"action":"insert","lines":["  "]}]}],[{"group":"doc","deltas":[{"start":{"row":77,"column":2},"end":{"row":78,"column":0},"action":"insert","lines":["",""]},{"start":{"row":78,"column":0},"end":{"row":78,"column":2},"action":"insert","lines":["  "]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":2},"end":{"row":78,"column":3},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":3},"end":{"row":78,"column":4},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":4},"end":{"row":78,"column":5},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":5},"end":{"row":78,"column":6},"action":"insert","lines":["v"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":6},"end":{"row":78,"column":7},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":7},"end":{"row":78,"column":8},"action":"insert","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":8},"end":{"row":78,"column":9},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":9},"end":{"row":78,"column":10},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":10},"end":{"row":78,"column":11},"action":"insert","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":11},"end":{"row":78,"column":12},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":12},"end":{"row":78,"column":13},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":13},"end":{"row":78,"column":14},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":14},"end":{"row":78,"column":15},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":15},"end":{"row":78,"column":16},"action":"insert","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":12},"end":{"row":78,"column":16},"action":"remove","lines":["disc"]},{"start":{"row":78,"column":12},"end":{"row":78,"column":21},"action":"insert","lines":["discovery"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":21},"end":{"row":78,"column":22},"action":"insert","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":22},"end":{"row":78,"column":23},"action":"insert","lines":["b"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":23},"end":{"row":78,"column":24},"action":"insert","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":24},"end":{"row":78,"column":25},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":25},"end":{"row":78,"column":26},"action":"insert","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":26},"end":{"row":78,"column":27},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":27},"end":{"row":78,"column":28},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":28},"end":{"row":78,"column":29},"action":"insert","lines":["\""]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":29},"end":{"row":78,"column":30},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":30},"end":{"row":78,"column":31},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":31},"end":{"row":78,"column":32},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":32},"end":{"row":78,"column":33},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":29},"end":{"row":78,"column":33},"action":"remove","lines":["sotr"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":29},"end":{"row":78,"column":30},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":30},"end":{"row":78,"column":31},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":30},"end":{"row":78,"column":31},"action":"remove","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":30},"end":{"row":78,"column":31},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":31},"end":{"row":78,"column":32},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":32},"end":{"row":78,"column":33},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":33},"end":{"row":78,"column":34},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":34},"end":{"row":78,"column":35},"action":"insert","lines":["g"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":35},"end":{"row":78,"column":36},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":36},"end":{"row":78,"column":37},"action":"insert","lines":["\""]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":37},"end":{"row":78,"column":38},"action":"insert","lines":[","]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":38},"end":{"row":78,"column":39},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":39},"end":{"row":78,"column":40},"action":"insert","lines":["_"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":40},"end":{"row":78,"column":41},"action":"insert","lines":["A"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":41},"end":{"row":78,"column":42},"action":"insert","lines":["P"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":42},"end":{"row":78,"column":43},"action":"insert","lines":["I"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":43},"end":{"row":78,"column":44},"action":"insert","lines":["_"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":44},"end":{"row":78,"column":45},"action":"insert","lines":["V"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":45},"end":{"row":78,"column":46},"action":"insert","lines":["D"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":45},"end":{"row":78,"column":46},"action":"remove","lines":["D"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":44},"end":{"row":78,"column":45},"action":"remove","lines":["V"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":44},"end":{"row":78,"column":45},"action":"insert","lines":["V"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":45},"end":{"row":78,"column":46},"action":"insert","lines":["E"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":46},"end":{"row":78,"column":47},"action":"insert","lines":["R"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":47},"end":{"row":78,"column":48},"action":"insert","lines":["S"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":48},"end":{"row":78,"column":49},"action":"insert","lines":["I"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":49},"end":{"row":78,"column":50},"action":"insert","lines":["O"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":50},"end":{"row":78,"column":51},"action":"insert","lines":["N"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":51},"end":{"row":78,"column":52},"action":"insert","lines":[","]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":52},"end":{"row":78,"column":53},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":53},"end":{"row":78,"column":54},"action":"insert","lines":["h"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":54},"end":{"row":78,"column":55},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":55},"end":{"row":78,"column":56},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":56},"end":{"row":78,"column":57},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":57},"end":{"row":78,"column":58},"action":"insert","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":58},"end":{"row":78,"column":59},"action":"insert","lines":["h"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":59},"end":{"row":78,"column":60},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":60},"end":{"row":78,"column":61},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":61},"end":{"row":78,"column":62},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":62},"end":{"row":78,"column":63},"action":"insert","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":63},"end":{"row":79,"column":0},"action":"insert","lines":["",""]},{"start":{"row":79,"column":0},"end":{"row":79,"column":2},"action":"insert","lines":["  "]}]}],[{"group":"doc","deltas":[{"start":{"row":79,"column":2},"end":{"row":79,"column":3},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":79,"column":3},"end":{"row":79,"column":4},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":79,"column":4},"end":{"row":79,"column":5},"action":"insert","lines":["y"]}]}],[{"group":"doc","deltas":[{"start":{"row":79,"column":2},"end":{"row":79,"column":5},"action":"remove","lines":["try"]},{"start":{"row":79,"column":2},"end":{"row":82,"column":11},"action":"insert","lines":["try:","    # TODO: write code...","  except Exception, e:","    raise e"]}]}],[{"group":"doc","deltas":[{"start":{"row":80,"column":4},"end":{"row":80,"column":25},"action":"remove","lines":["# TODO: write code..."]}]}],[{"group":"doc","deltas":[{"start":{"row":80,"column":4},"end":{"row":80,"column":5},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":80,"column":5},"end":{"row":80,"column":6},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":80,"column":6},"end":{"row":80,"column":7},"action":"insert","lines":["q"]}]}],[{"group":"doc","deltas":[{"start":{"row":80,"column":7},"end":{"row":80,"column":8},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":80,"column":8},"end":{"row":80,"column":9},"action":"insert","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":80,"column":9},"end":{"row":80,"column":10},"action":"insert","lines":[" "]}]}]]},"ace":{"folds":[],"scrolltop":1206,"scrollleft":0,"selection":{"start":{"row":103,"column":0},"end":{"row":103,"column":0},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":79,"state":"start","mode":"ace/mode/python"}},"timestamp":1420071051967}