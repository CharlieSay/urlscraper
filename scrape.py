import urllib2
response = urllib2.urlopen('http://python.org/')
print(response.read())