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
state = jsonObject['state']['xy']


if (state == [0.144, 0.1738]):

    statebulb = '{"xy":[0.3136, 0.3216]}'
    x = reqs.put(updateurl , data = statebulb)
else:
    
    statebulb = '{"xy":[0.144, 0.1738]}'
    x = reqs.put(updateurl , data = statebulb)
        