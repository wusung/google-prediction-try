class GooglePrediction:
    def __init__(self):
        print "init"
    def upload(self, name, directory):
        print "upload"
    def train(self, data, model_name):
        print "train"

g = GooglePrediction()
g.train(name="test.csv", directory='https://www.dropbox.com/s/vt3w7dlaey8kr27/IF1404.txt?dl=1')
g.upload("", "")
g.predict(model='test012', sample = DataFrame(xxxxx))  
