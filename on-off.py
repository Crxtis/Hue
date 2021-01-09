import requests as reqs
import json
ip = "192.168.0.62"
username = "yjtesHyWJDPH6JaSE67iXDxhZNqXCM4UXNO34pbq"
curtis = "16"
fullurl = ("http://" + ip + "/api/" + username + "/lights/" + curtis )
updateurl = ("http://" + ip + "/api/" + username + "/lights/" + curtis + "/state" )
print (fullurl)


response = reqs.get(fullurl)
jsonstring = response.text
jsonObject = json.loads(jsonstring)
state = jsonObject['state']['on']


if (state == True):
    statebulb = '{"on":false}'
    x = reqs.put(updateurl , data = statebulb)
else:
    statebulb = '{"on":true}'
    x = reqs.put(updateurl , data = statebulb)

        
