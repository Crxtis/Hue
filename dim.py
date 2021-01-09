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
state = jsonObject['state']['bri']
print(state)


if (state == 254):

    statebulb = '{"bri":55}'
    x = reqs.put(updateurl , data = statebulb)
else:
    
    statebulb = '{"bri":254}'
    x = reqs.put(updateurl , data = statebulb)


