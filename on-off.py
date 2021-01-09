import requests as reqs
import json
ip = "bridge ip"
username = "hue light username"
ln = "your light numer"
fullurl = ("http://" + ip + "/api/" + username + "/lights/" + ln )
updateurl = ("http://" + ip + "/api/" + username + "/lights/" + ln + "/state" )


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

        
