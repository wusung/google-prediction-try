import csv
import logging
import simplejson
import sys
import urllib
import urllib2


def predict(target, auth, text):
  request_data = {
      'data': {
          'input': {
              'text': text,
          }
      }
  }
  request = urllib2.Request(
      'https://www.googleapis.com/prediction/v1/training/%s/predict' % target,
      data=simplejson.dumps(request_data),
      headers={
          "Authorization": "GoogleLogin auth=%s" % auth,
          "Content-Type": "application/json",
      })
  response = urllib2.urlopen(request)
  response_data = simplejson.load(response)
  return response_data['data']['output']['output_label']

def main(args):
  infile, auth, target = args[1:4]
  reader = csv.reader(open(infile))
  count = 0
  correct = 0
  for tag, text, domain in reader:
    count += 1
    retries = 0
    while retries < 10:
      try:
        result = predict(target, auth, [text.strip('\r\n\\n'), domain])
        break
      except urllib2.HTTPError, e:
        retries += 1
    if result == tag:
      correct += 1
    else:
      print ("Incorrectly predicted %r (%s) as %s (should be %s)"
             % (text, domain, result, tag))
  print "%d of %d predicted correctly." % (correct, count)


if __name__ == '__main__':
  main(sys.argv)