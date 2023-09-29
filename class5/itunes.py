import json
import sys
import requests

if len(sys.argv) !=2:
    exit()

#get responses from the server
response = requests.get("http://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent =2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])