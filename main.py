 #!/usr/bin/python
import pprint

from model import APIManager
from model import HostedModel
from model import TrainedModel
from flyberry.machine_learning.google_prediction import GooglePrediction

# client_id = "222222222222.apps.googleusercontent.com"
# client_secret = "xxxxxxxxxxxxxxxx_YYYYYYY"
# redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
# base_url = r"https://accounts.google.com/o/oauth2/"
# authorization_code = ""
# access_token = ""

# def retrieve_authorization_code():
#   authorization_code_req = {
#     "response_type": "code",
#     "client_id": client_id,
#     "redirect_uri": redirect_uri,
#     "scope": (r"https://www.googleapis.com/auth/userinfo.profile" +
#               r" https://www.googleapis.com/auth/userinfo.email" +
#               r" https://www.googleapis.com/auth/prediction")
#     }
 
#   r = requests.get(base_url + "auth?%s" % urlencode(authorization_code_req),
#                   allow_redirects=False)
#   print ""
#   url = r.headers.get('location')
#   Popen(["open", url])
 
#   authorization_code = raw_input("\nAuthorization Code >>> ")
#   return authorization_code

googlePrediction = GooglePrediction()
#googlePrediction.upload(name='creature.txt', directory='./')
# googlePrediction.upload(name='test.csv', directory='https://www.dropbox.com/s/vt3w7dlaey8kr27/IF1404.txt?dl=1' ) 
#googlePrediction.train(data='flyberry/creature.txt', model_name='Creature')
#googlePrediction.list(model='creature')
# p = googlePrediction.predict(model='Language', sample='dog')  
# print p

p = googlePrediction.get(model='Creature')
p = googlePrediction.predict(model='Creature', sample=(77.50,-55.33,'Animal'))
print p
p = googlePrediction.predict(model='Creature', sample=(78.00,-55.33,'Animal'))
print p
p = googlePrediction.predict(model='Creature', sample=(78.50,-55.33,'Animal'))
print p
