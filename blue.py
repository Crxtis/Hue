import requests as reqs
import json
ip = "bridge ip"
username = "hue light username"
ln = "your light number"
fullurl = ("http://" + ip + "/api/" + username + "/lights/" + ln )
updateurl = ("http://" + ip + "/api/" + username + "/lights/" + ln + "/state" )

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
        
