 #!/usr/bin/python
import pprint
import json

from flyberry.machine_learning.google_prediction import GooglePrediction

googlePrediction = GooglePrediction()
googlePrediction.upload(name='creature.txt', directory='./')
googlePrediction.upload(name='test.csv', directory='https://www.dropbox.com/s/vt3w7dlaey8kr27/IF1404.txt?dl=1' ) 
result = googlePrediction.get(model='Creature')
