import requests
import json

search='mass_effect'
url='https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch=%s' % search
print(url)
response=requests.get(url)
#print(response.text)
rawjson=json.loads(response.text)

for results in rawjson['query']['search']:
    print(results['title'])
    print(results['snippet'])
