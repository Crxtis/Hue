import requests as reqs
import json
ip = "192.168.0.62"
username = "yjtesHyWJDPH6JaSE67iXDxhZNqXCM4UXNO34pbq"
curtis = "16"
fullurl = ("http://" + ip + "/api/" + username + "/lights/" + curtis )
updateurl = ("http://" + ip + "/api/" + username + "/lights/" + curtis + "/state" )

response = reqs.get(fullurl)
jsonstring = response.text
jsonObject = json.loads(jsonstring)
state = jsonObject['state']['bri']
print(state)


if (state == 254):

    statebulb = '{"bri":55}'
    x = reqs.put(updateurl , data = statebulb)
else:
    
    statebulb = '{"bri":254}'
    x = reqs.put(updateurl , data = statebulb)


