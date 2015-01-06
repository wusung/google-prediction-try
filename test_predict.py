 #!/usr/bin/python
import pprint
import json

from flyberry.machine_learning.google_prediction import GooglePrediction

googlePrediction = GooglePrediction()

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
