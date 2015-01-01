#!/usr/bin/python

from flyberry.machine_learning.google_prediction import GooglePrediction

googlePrediction = GooglePrediction()
googlePrediction.upload(name='README.md', directory='./')
googlePrediction.upload(name='test.csv', directory='https://www.dropbox.com/s/vt3w7dlaey8kr27/IF1404.txt?dl=1' ) 
googlePrediction.train(data='test.csv', model_name='test012',parameter1='xxxx', parameter2='dddd')  
googlePrediction.predict(model='test012', sample = DataFrame(xxxxx))  
