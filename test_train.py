 #!/usr/bin/python
import pprint
import json

from flyberry.machine_learning.google_prediction import GooglePrediction

googlePrediction = GooglePrediction()
googlePrediction.train(data='flyberry/test.csv', model_name='test12')
googlePrediction.train(data='flyberry/creature.csv', model_name='Creature')
