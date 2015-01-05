# Prediction Reference

## Prerequist

## Installation

## Upload example 1: Upload local file to Google Storage

    googlePrediction = GooglePrediction()
    googlePrediction.upload(name='creature.txt', directory='./')
    
## Upload example 2: Upload web file to Google Storage

    googlePrediction = GooglePrediction()
    googlePrediction.upload(name='creature.txt', directory='https://www.dropbox.com/s/vt3w7dlaey8kr27/IF1404.txt?dl=1')

## Train example:

    googlePrediction = GooglePrediction()
    googlePrediction.train(data='flyberry/creature.txt', model_name='Creature')

## Prediction example: 

    googlePrediction = GooglePrediction()
    p = googlePrediction.predict(model='Creature', sample=(77.50,-55.33,'Animal'))