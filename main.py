#!/usr/bin/python

from flyberry.machine_learning.google_prediction import GooglePrediction

pred = GooglePrediction()
pred.upload(name='test.csv', directory='https://www.dropbox.com/s/vt3w7dlaey8kr27/IF1404.txt?dl=1' ) 
pred.train(data='test.csv', model_name='test012',parameter1='xxxx', parameter2='dddd')  
pred.predict(model='test012', sample = DataFrame(xxxxx))  
