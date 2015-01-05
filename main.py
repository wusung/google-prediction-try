 #!/usr/bin/python
import pprint
import json

from model import APIManager
from model import HostedModel
from model import TrainedModel
from flyberry.machine_learning.google_prediction import GooglePrediction

googlePrediction = GooglePrediction()
#googlePrediction.upload(name='creature.txt', directory='./')
# googlePrediction.upload(name='test.csv', directory='https://www.dropbox.com/s/vt3w7dlaey8kr27/IF1404.txt?dl=1' ) 
# googlePrediction.train(data='flyberry/test.csv', model_name='test12')
#googlePrediction.list(model='creature')
# p = googlePrediction.predict(model='Language', sample='dog')  
# print p

result = googlePrediction.get(model='Creature')
p = googlePrediction.predict(model='Creature', sample=[
    (77.50,-55.33,'Animal'), 
    (78.00,-55.33,'Animal'),
    (78.50,-55.33,'Animal')])
print p
# p = googlePrediction.predict(model='Creature', sample=(77.50,-55.33,'Animal'))
# print p
# p = googlePrediction.predict(model='Creature', sample=(78.00,-55.33,'Animal'))
# print p
# p = googlePrediction.predict(model='Creature', sample=(78.50,-55.33,'Animal'))
# print p
