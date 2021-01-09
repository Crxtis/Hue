import requests as reqs
import json
ip = "bridge ip"
username = "hue light username"

fullurl = ("http://" + ip + "/api/" + username + "/lights/" )




response = reqs.get(fullurl)
jsonstring = response.text
jsonObject = json.loads(jsonstring)




print(jsonObject)

