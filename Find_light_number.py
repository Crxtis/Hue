import requests as reqs
import json
ip = "192.168.0.62"
username = "yjtesHyWJDPH6JaSE67iXDxhZNqXCM4UXNO34pbq"

fullurl = ("http://" + ip + "/api/" + username + "/lights/" )




response = reqs.get(fullurl)
jsonstring = response.text
jsonObject = json.loads(jsonstring)




print(jsonObject)

