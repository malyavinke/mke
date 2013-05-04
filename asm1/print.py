import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
d = json.load(response)
print len(d)
arr = d['results']
for key in arr:
	print 'text: ', key['text']
	print
